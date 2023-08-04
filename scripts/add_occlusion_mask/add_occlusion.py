import json
import os
import numpy as np
import pdb
import cv2
import copy
import ipdb
from tqdm import tqdm

def process_pose(rotation):
    if isinstance(rotation, str):
        return rotation
    if rotation >= 0 and rotation < 30:
        pose = 'back_pose'            
    elif rotation > 60 and rotation <= 120:
        pose = 'right_pose' 
    elif rotation > 150 and rotation <= 210:
        pose = 'front_pose'
    elif rotation > 240 and rotation <= 300:
        pose = 'left_pose'        
    elif rotation > 330:
        pose = 'back_pose'   
    else:
        pose = 'None'       
    return pose

def add_pose(scene):
    for obj in scene['objects']:
        rotation = obj['rotation']
        shape = obj['shape']
        if shape in ["road", "utility", "mountain", "tandem"]:
            pose_degree = (-rotation + 140) % 360
        else:
            pose_degree = (- rotation + 50) % 360
        pose = process_pose(pose_degree)

        obj['pose'] = pose
        obj['pose_degree'] = pose_degree
    return scene


def to_str(img):
    pre = 0
    has = 0
    lis = []
    for _x in img:
        if _x == pre:
            has += 1
        else:    
            lis.append(has)
            pre = 1-pre
            has = 1
    if has != 0:
        lis.append(has)
    return ','.join([str(it) for it in lis])


def str_to_biimg(imgstr):

    img=[]
    cur = 0

    for num in imgstr.strip().split(','):
        num = int(num)
        img += [cur] * num
        cur = 1 - cur
    img = np.array(img).astype(np.uint8)
    img = np.asfortranarray(img.reshape((480, 640)))

    # cv2.imwrite("output/test_mask.png", img*255)
    return img
    

def _compute_occlusion(mask_before, mask_after, min_part_pixel = 20, vis = False):

    mask_before = str_to_biimg(mask_before)
    mask_after = str_to_biimg(mask_after)
    
    visible_before = True

    # For the part invisible at all
    if np.sum(mask_before) < min_part_pixel:
        visible_before = False
        # probably it will have some value below, but if visible_before = False,
        # it will not be included into the scene file

    # only the part which is occluded now and visible before
    occlussion = mask_before - mask_before * mask_after

    # area
    sum_occlussion = int(np.sum(occlussion))
    sum_mask_before = int(np.sum(mask_before))

    if sum_mask_before - sum_occlussion < 1.0:
        # fully occluded and before is visible
        is_occluded = 2

    elif sum_occlussion > 15.0 and sum_mask_before - sum_occlussion > 15.0:
        # means 1. sum_mask_before - sum_occlussion = sum_before*after > 5.0
        # other aspect, sum_occlusion = sum_before - sum_before*after < sum_before - 5
        # i.e. 5 < sum_occlusion < sum_before - 5
        is_occluded = 1

    elif sum_occlussion < 1.0:
        is_occluded = 0

    else:
        # the condition above will not cover all the situation, for the others,
        # the situation is too ambiguous, just assign -1 and be skipped later 
        is_occluded = -1

    # if vis:
    #     cv2.imwrite('mask_before.png', mask_before / np.max(mask_before) * 255)
    #     cv2.imwrite('mask_after.png', mask_after / np.max(mask_after) * 255)
    #     cv2.imwrite('occlussion.png', occlussion / np.max(occlussion) * 255)
    #     import ipdb
    #     ipdb.set_trace()
    
    occlussion = occlussion.astype(int).flatten().tolist()

    return is_occluded, to_str(occlussion), visible_before


def compute_occlusion(scene, obj, obj_index):
    # 0: not occluded, 1: partially, 2, fully 
    occlusion = {}
    # print(obj_index)
    obj = obj['obj_mask_box']['0']
    obj_mask_box = scene['obj_mask_box'][obj_index]
    for part_name, mask in obj.items():
        if part_name == 'info':
            continue
        if part_name in obj_mask_box:
            mask_after = obj_mask_box[part_name][1]
            mask_before = mask[1]
            occluded, mask_occlusion, visible_before = _compute_occlusion(mask_before, mask_after, vis = part_name == 'obj')

        else:
            print("not in the object map box")
            with open("log.txt", "a") as f:
                f.write(f"{scene['image_filename']}, {obj_index}, {part_name}\n")
            print(f"{scene['image_filename']}, {obj_index}, {part_name}")
            occluded = 2
            mask_occlusion = mask_before
            visible_before = False if np.sum(mask_before) < 20 else True

        if part_name == 'obj' and occluded == -1:
            occluded = 0
            # ipdb.set_trace()

        if occluded > 0 and visible_before or part_name == 'obj':
            occlusion[part_name] = [occluded, mask_occlusion, str(visible_before)]

    return occlusion

def find_occluded_by(mask, all_objects_mask, this_obj_id):
    # mask is the area being occluded
    if mask[0] == 0:
        return -1, 0
    this_mask = str_to_biimg(mask[1])
    occluded = mask[0]

    max_area = 0
    occluded_by = -1

    for obj_id, obj_mask_img in all_objects_mask.items():
        # obj_mask_img = str_to_biimg(obj_mask)
        intersect_area = np.sum(obj_mask_img * this_mask)
        if max_area < intersect_area and this_obj_id != obj_id:
            occluded_by = obj_id
            max_area = intersect_area

    if occluded_by == -1 and occluded > 0:
        occluded = -1
        # pdb.set_trace()

    return occluded_by, occluded


def compute_occlusion_relationship(scene):
    all_objects_mask = {obj_id : str_to_biimg(masks['obj'][1]) for obj_id, masks in scene['obj_mask_box'].items()}
    occlusion_mask = scene['occlusion']

    for obj_id, name_mask in occlusion_mask.items():
        name_to_drop = []
        for name, mask in name_mask.items():
            by_index, occluded = find_occluded_by(mask, all_objects_mask, obj_id)
            if occluded > 0:
                scene['occlusion'][obj_id][name].append(by_index) 
                scene['occlusion'][obj_id][name][0] = occluded 
            elif name == 'obj' and occluded == -1:
                name_to_drop = list(name_mask.keys())
                break
            else:
                name_to_drop.append(name)
        for name in name_to_drop:
            if name != 'obj':
                scene['occlusion'][obj_id].pop(name, None)
    
if __name__ == '__main__':
    import pdb

    new_dir = "/home/xingrui/publish/superclevr_3D_questions/output/ver_mask_new/scenes-split"
    new_dir_occlusion = "/home/xingrui/publish/superclevr_3D_questions/output/ver_mask_new/scenes_with_occlusion"
    output_scene_file = "/home/xingrui/publish/superclevr_3D_questions/output/ver_mask_new/superCLEVR_scenes_210k_occlusion_stricker_0412.json"

    original_super_clevr_scene = "/home/xingrui/publish/superclevr_3D_questions/output/ver_mask_new/superCLEVR_scenes_210k.json"
    # original_super_clevr_scene = "/home/xingrui/vqa/super-clevr-gen/output/ver_mask_new/superCLEVR_scenes_occlusion.json"

    with open(original_super_clevr_scene, 'r') as f:
        new_scene = json.load(f)
    
    ori_scenes = copy.deepcopy(new_scene['scenes'][:])
    
    new_scene['scenes'] = []

    find_new = False
    ori_idx = ''
    scene = {}

    # idx = 19999-1
    idx = -1

    read_scene_dict = {}

    for scene_file in tqdm(sorted(os.listdir(new_dir))):
        with open(os.path.join(new_dir, scene_file)) as f:
            obj = json.load(f)
        read_scene_dict[scene_file] = obj

    sorted_list = sorted(os.listdir(new_dir))
    # for scene_file in tqdm(sorted_list[130081:]):
    for scene_file in tqdm(sorted_list[:]):

        if len(scene_file.split("_")) < 4:
            continue

        obj = read_scene_dict[scene_file]
        
        ori_scene_name = "_".join(scene_file.split("_")[:-1])
        
        if ori_idx != ori_scene_name:
            
            if ori_idx != '':
                compute_occlusion_relationship(scene)
                scene_with_occlusion = add_pose(scene)
                new_scene['scenes'].append(scene_with_occlusion)

                with open(os.path.join(new_dir_occlusion, f'scene_occlusion_{idx:06d}.json'), 'w') as ww:
                    json.dump(scene_with_occlusion, ww)
            idx += 1     
            if idx % 200 == 0:
                print(f"To index {idx}")

            if idx >= len(ori_scenes):
            # if idx >= len(ori_scenes) or idx > 2:
                break
            scene = ori_scenes[idx]
            scene['occlusion'] = {}

            ori_idx = ori_scene_name
            find_new = True
        else:
            find_new = False

        image_index = obj['image_index']
        img_index, obj_index = image_index.split("_")

        scene['occlusion'][obj_index] = compute_occlusion(scene, obj, obj_index)
print(f"Generate {idx} scenes")
with open(output_scene_file, 'w') as f:
    json.dump(new_scene, f)



    




