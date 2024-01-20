# Image Generation of Super-CLEVR-3D

The image of Super-CLEVR-3D are using the same setting of [Super-CLEVR](https://github.com/Lizw14/Super-CLEVR/tree/main/image_generation). But the original Super-CLEVR dataset doesn't record the occlusion part of each object, which will be uilizied to generate occlusion question.
So we need to re-render the objects from the scene one-by-one and then computer the mask of occluded / visible part of each object.

If you want to generate the image yourself, you can run `scripts/render_images_3D.sh` at the root directory. In detail, the generation contains four steps.

### 1. Rerender Superclevr image.
This is the same image generation process as [Super-CLEVR](https://github.com/Lizw14/Super-CLEVR/tree/main/image_generation), which you should first setup the environment following according to their instructions. Although the setting is the same, **we re-render to add the camera parameters into the annotation files, as they are randomly assigned in each scene.**

```
cd image_generation

# 1.rerender Superclevr image, add the camera attributions
/your/path/to/blender --background \
    --python super_restore_render_images.py --\
    --start_idx 0 \
    --num_image 30000 \
    --use_gpu 1 \
    --shape_dir /home/xingrui/data/CGPart \
    --model_dir data/save_models_1/ \
    --properties_json data/properties_cgpart.json \
    --margin 0.1 \
    --save_blendfiles 0 \
    --max_retries 150 \
    --width 640 \
    --height 480 \
    --output_image_dir ../output/ver_mask_30k/images/ \
    --output_scene_dir ../output/ver_mask_30k/scenes/ \
    --output_blend_dir ../output/ver_mask_30k/blendfiles \
    --output_scene_file ../output/ver_mask_30k/superCLEVR_scenes.json \
    --is_part 1
```

### 2. Split the scene file.

In order to add occlusion relationship into the annotations, we will re-render the each object one by one and compute their occlusions in the future. Here we need to create the scene files for each of them, to render them independently in the scene.

```
python add_occlusion_mask/split_scenes.py \
    --original_super_clevr_scene /home/xingrui/publish/3D-Aware-VQA/superclevr-3D-question/output/ver_mask_30k_copy/last_9000.json \
    --output_scene_file /home/xingrui/publish/3D-Aware-VQA/superclevr-3D-question/output/ver_mask_30k_copy/superCLEVR_scenes_split_last_9000.json
```

### 3. Render each objects.

```
/your/path/to/blender --background \
    --python super_restore_render_images_split.py -- \
    --start_idx 50000 \
    --num_images 8877 \
    --use_gpu 1 \
    --shape_dir ~/data/CGPart \
    --model_dir data/save_models_1/ \
    --properties_json data/properties_cgpart.json \
    --margin 0.1 \
    --save_blendfiles 0 \
    --max_retries 150 \
    --width 640 \
    --height 480 \
    --output_image_dir ../output/ver_mask_30k_copy/images-split/ \
    --output_scene_dir ../output/ver_mask_30k_copy/scenes-split/ \
    --output_blend_dir ../output/ver_mask_30k_copy/blendfiles-split/ \
    --output_scene_file ../output/ver_mask_30k_copy/superCLEVR_scenes_split_9000.json \
    --is_part 1 \
    --load_scene 1 \
    --clevr_scene_path /home/xingrui/publish/3D-Aware-VQA/superclevr-3D-question/output/ver_mask_30k_copy/superCLEVR_scenes_split_last_9000.json
```

### 4. Compute the occlusion area and add them to the annotation files.

```
python add_occlusion_mask/add_occlusion.py \
    --splitted_scene /home/xingrui/publish/3D-Aware-VQA/superclevr-3D-question/output/ver_mask_30k_copy/scenes-split \
    --scenes_with_occlusion /home/xingrui/publish/3D-Aware-VQA/superclevr-3D-question/output/ver_mask_30k_copy/scenes_with_occlusion \
    --output_scene_file /home/xingrui/publish/3D-Aware-VQA/superclevr-3D-question/output/ver_mask_30k_copy/superCLEVR_scenes_occlusion_9000.json \
    --original_super_clevr_scene /home/xingrui/publish/3D-Aware-VQA/superclevr-3D-question/output/ver_mask_30k_copy/last_9000.json
```

