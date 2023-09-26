# split_scene_to_single_objects
import argparse
import json
import os
import ipdb

parser = argparse.ArgumentParser()
parser.add_argument('--original_super_clevr_scene', help='the path of superclevr scene file')
parser.add_argument('--output_scene_file', help='the path of file after place objects into individual scenes')
args = parser.parse_args()


def splitScenes(args):
    """Split the objects into indivisual scenes."""

    with open(args.original_super_clevr_scene, 'r') as f:
        superclevr_scene = json.load(f)

    new_scene = {}
    new_scene['info'] = superclevr_scene['info']
    new_scene['scenes'] = []

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

    with open(args.output_scene_file, 'w') as f:
        f.write(json.dumps(new_scene))

    print("Finish, {} scenes in total".format(all_scene))
# 136549


if __name__ == '__main__':
    splitScenes(args)