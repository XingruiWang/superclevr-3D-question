cd image_generation

# 1.rerender Superclevr image, add the camera attributions
# CUDA_VISIBLE_DEVICES=3 \
# ~/packages/blender-2.79b-linux-glibc219-x86_64/blender --background \
#     --python super_restore_render_images.py --\
#     --start_idx 0 \
#     --num_image 10 \
#     --use_gpu 1 \
#     --shape_dir /home/xingrui/data/CGPart \
#     --model_dir data/save_models_1/ \
#     --properties_json data/properties_cgpart.json \
#     --margin 0.1 \
#     --save_blendfiles 0 \
#     --max_retries 150 \
#     --width 640 \
#     --height 480 \
#     --output_image_dir ../output/ver_mask_10/images/ \
#     --output_scene_dir ../output/ver_mask_10/scenes/ \
#     --output_blend_dir ../output/ver_mask_10/blendfiles \
#     --output_scene_file ../output/ver_mask_10/superCLEVR_scenes.json \
#     --is_part 1

# python add_occlusion_mask/split_scenes.py \
#     --original_super_clevr_scene /home/xingrui/publish/superclevr_3D_questions/output/ver_mask_10/superCLEVR_scenes.json \
#     --output_scene_file /home/xingrui/publish/superclevr_3D_questions/output/ver_mask_10/superCLEVR_scenes_split.json


# 3. generate splitted scene
# CUDA_VISIBLE_DEVICES=3 ~/packages/blender-2.79b-linux-glibc219-x86_64/blender --background \
#     --python super_restore_render_images_split.py -- \
#     --start_idx 0 \
#     --num_images 77 \
#     --use_gpu 1 \
#     --shape_dir ~/data/CGPart \
#     --model_dir data/save_models_1/ \
#     --properties_json data/properties_cgpart.json \
#     --margin 0.1 \
#     --save_blendfiles 0 \
#     --max_retries 150 \
#     --width 640 \
#     --height 480 \
#     --output_image_dir ../output/ver_mask_10/images-split/ \
#     --output_scene_dir ../output/ver_mask_10/scenes-split/ \
#     --output_blend_dir ../output/ver_mask_10/blendfiles-split/ \
#     --output_scene_file ../output/ver_mask_10/superCLEVR_scenes_split.json \
#     --is_part 1 \
#     --load_scene 1 \
#     --clevr_scene_path /home/xingrui/publish/superclevr_3D_questions/output/ver_mask_10/superCLEVR_scenes_split.json

# 4.
python add_occlusion_mask/add_occlusion.py