cd image_generation

# 1.rerender Superclevr image, add the camera attributions
CUDA_VISIBLE_DEVICES=3 \
~/packages/blender-2.79b-linux-glibc219-x86_64/blender --background \
    --python super_restore_render_images.py --\
    --start_idx 0 \
    --num_image 77 \
    --use_gpu 1 \
    --shape_dir /home/xingrui/data/CGPart \
    --model_dir data/save_models_1/ \
    --properties_json data/properties_cgpart.json \
    --margin 0.1 \
    --save_blendfiles 0 \
    --max_retries 150 \
    --width 640 \
    --height 480 \
    --camera_jitter 0 \
    --output_image_dir ../output/ver_texture_new/images/ \
    --output_scene_dir ../output/ver_texture_new/scenes/ \
    --output_blend_dir ../output/ver_texture_new/blendfiles \
    --output_scene_file ../output/ver_texture_new/superCLEVR_scenes.json \
    --is_part 1 \
    --add_texture \
    --load_scene 1 \
    --clevr_scene_path /home/xingrui/publish/superclevr_3D_questions/output/ver_mask_new/superCLEVR_scenes_210k.json
    # --clevr_scene_path /home/xingrui/publish/superclevr_3D_questions/output/z_direction/superCLEVR_scenes.json
    # --clevr_scene_path ../output/ver_mask/superCLEVR_scenes.json 


# CUDA_VISIBLE_DEVICES=2 \
# ~/packages/blender-2.79b-linux-glibc219-x86_64/blender --background \
#     --python super_restore_render_images_split.py -- \
#     --start_idx 0 \
#     --use_gpu 1 \
#     --shape_dir ~/data/CGPart \
#     --model_dir data/save_models_1/ \
#     --properties_json data/properties_cgpart.json \
#     --margin 0.1 \
#     --save_blendfiles 0 \
#     --max_retries 150 \
#     --width 640 \
#     --height 480 \
#     --output_image_dir ../output/ver_mask_new/images-split/ \
#     --output_scene_dir ../output/ver_mask_new/scenes-split/ \
#     --output_blend_dir ../output/ver_mask_new/blendfiles-split/ \
#     --output_scene_file ../output/ver_mask_new/superCLEVR_scenes_split.json \
#     --is_part 1 \
#     --load_scene 1 \
#     --clevr_scene_path ../output/ver_mask_new/superCLEVR_scenes_splitted.json








cd ..

