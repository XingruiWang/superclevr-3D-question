'''
This is to combine the scene file together aftet generate
'''

import os
import json

new_dir_occlusion = "/home/xingrui/vqa/super-clevr-gen/output/ver_mask_new/scenes_with_occlusion"

all_scene = {"info": {"version": "1.0", "license": "Creative Commons Attribution (CC-BY 4.0)", "date": "03/11/2023", "split": "new"}, "scenes": []}
for idx in range(0, 20999):
    with open(os.path.join(new_dir_occlusion, f'scene_occlusion_{idx}.json')) as ww:
        
        scene_with_occlusion = json.load(ww)
    all_scene['scenes'].append(scene_with_occlusion)

with open(os.path.join('/home/xingrui/vqa/super-clevr-gen/output/ver_mask_new', 'superCLEVR_scenes_210k_occlusion-recovered.json'), 'w') as ww:
    json.dump(all_scene, ww)
