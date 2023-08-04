# split_scene_to_single_objects


import json
import os
import ipdb

original_super_clevr_scene = "/home/xingrui/publish/superclevr_3D_questions/output/ver_mask_new/superCLEVR_scenes_210k.json"
output_scene_file = "/home/xingrui/publish/superclevr_3D_questions/output/ver_mask_new/superCLEVR_scenes_splitted.json"

with open(original_super_clevr_scene, 'r') as f:
    superclevr_scene = json.load(f)

ipdb.set_trace()
new_scene = {}
new_scene['info'] = superclevr_scene['info']
new_scene['scenes'] = []

idx = 0
all_scene = 0
for s in superclevr_scene['scenes']:
    for i, obj in enumerate(s['objects']):
        newScene = {}
        img_name = s['image_filename'].split(".")[0]
        newScene['image_filename'] = "{}_obj_{}.png".format(img_name,i)
        newScene['image_index'] = "{}_{}".format(s['image_index'], i)
        newScene['directions'] = s['directions']
        newScene['camera_location'] = s['camera_location']
        newScene['split'] = s['split']
        newScene['object_index'] = i
        newScene['objects'] = [obj]
        new_scene['scenes'].append(newScene)
        all_scene += 1

with open(output_scene_file, 'w') as f:
    f.write(json.dumps(new_scene))

print("Finish, {} scenes in total".format(all_scene))
# 136549