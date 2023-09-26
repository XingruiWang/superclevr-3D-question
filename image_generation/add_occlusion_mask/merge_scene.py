# split_scene_to_single_objects


import json
import os
from tqdm import tqdm

def process_pose(rotation):
    if isinstance(rotation, str):
        return rotation
    if rotation <= 0 and rotation > 30:
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

original_super_clevr_scene = "/home/zhuowan_intern/xingrui/super-clevr-gen/ver_mask/superCLEVR_scenes_210k.json"
input_scene_file = "/home/zhuowan_intern/xingrui/super-clevr-gen/output/ver_mask_new/scenes_with_occlusion"
output_scene_file = "/home/zhuowan_intern/xingrui/super-clevr-gen/output/ver_mask_new/superCLEVR_scenes_1k_occlusion.json"

with open(original_super_clevr_scene, 'r') as f:
    new_scene = json.load(f)

new_scene['scenes'] = []

idx = 0

for scene in tqdm(os.listdir(input_scene_file)):
    idx += 1
    with open(os.path.join(input_scene_file, scene)) as f:
        scene_with_occlusion = json.load(f)
    scene_with_occlusion = add_pose(scene_with_occlusion)
    new_scene['scenes'].append(scene_with_occlusion)


with open(output_scene_file, 'w') as f:
    json.dump(new_scene, f)

print("Finish, {} in total".format(idx))





