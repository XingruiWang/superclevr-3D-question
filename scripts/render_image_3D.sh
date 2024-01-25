cd image_generation

# 1.rerender Superclevr image, add the camera attributions
# 32810， 35810， 38810
# CUDA_VISIBLE_DEVICES=2 \
# ~/packages/blender-2.79b-linux-glibc219-x86_64/blender --background \
#     --python super_restore_render_images.py --\
#     --start_idx 0 \
#     --num_image 30000 \
#     --use_gpu 1 \
#     --shape_dir /home/xingrui/data/CGPart \
#     --model_dir data/save_models_1/ \
#     --properties_json data/properties_cgpart.json \
#     --margin 0.1 \
#     --save_blendfiles 0 \
#     --max_retries 150 \
#     --width 640 \
#     --height 480 \
#     --output_image_dir ../output/ver_mask_30k/images/ \
#     --output_scene_dir ../output/ver_mask_30k/scenes/ \
#     --output_blend_dir ../output/ver_mask_30k/blendfiles \
#     --output_scene_file ../output/ver_mask_30k/superCLEVR_scenes.json \
#     --is_part 1

# python add_occlusion_mask/split_scenes.py \
#     --original_super_clevr_scene /home/xingrui/publish/3D-Aware-VQA/superclevr-3D-question/output/ver_mask_30k_copy/last_9000.json \
#     --output_scene_file /home/xingrui/publish/3D-Aware-VQA/superclevr-3D-question/output/ver_mask_30k_copy/superCLEVR_scenes_split_last_9000.json

# --num_images 58877
# 3. generate splitted scene
# CUDA_VISIBLE_DEVICES=3 ~/packages/blender-2.79b-linux-glibc219-x86_64/blender --background \
#     --python super_restore_render_images_split.py -- \
#     --start_idx 50000 \
#     --num_images 8877 \
#     --use_gpu 1 \
#     --shape_dir ~/data/CGPart \
#     --model_dir data/save_models_1/ \
#     --properties_json data/properties_cgpart.json \
#     --margin 0.1 \
#     --save_blendfiles 0 \
#     --max_retries 150 \
#     --width 640 \
#     --height 480 \
#     --output_image_dir ../output/ver_mask_30k_copy/images-split/ \
#     --output_scene_dir ../output/ver_mask_30k_copy/scenes-split/ \
#     --output_blend_dir ../output/ver_mask_30k_copy/blendfiles-split/ \
#     --output_scene_file ../output/ver_mask_30k_copy/superCLEVR_scenes_split_9000.json \
#     --is_part 1 \
#     --load_scene 1 \
#     --clevr_scene_path /home/xingrui/publish/3D-Aware-VQA/superclevr-3D-question/output/ver_mask_30k_copy/superCLEVR_scenes_split_last_9000.json

# # 4.
# python add_occlusion_mask/add_occlusion.py \
#     --splitted_scene /home/xingrui/publish/3D-Aware-VQA/superclevr-3D-question/output/ver_mask_30k_copy/scenes-split \
#     --output_scenes_dir /home/xingrui/publish/3D-Aware-VQA/superclevr-3D-question/output/ver_mask_30k_copy/scenes_with_occlusion \
#     --output_scene_file /home/xingrui/publish/3D-Aware-VQA/superclevr-3D-question/output/ver_mask_30k_copy/superCLEVR_scenes_occlusion_9000.json \
#     --original_super_clevr_scene /home/xingrui/publish/3D-Aware-VQA/superclevr-3D-question/output/ver_mask_30k_copy/last_9000.json

python add_occlusion_mask/add_occlusion.py \
    --splitted_scene /home/xingrui/publish/3D-Aware-VQA/superclevr-3D-question/output/ver_mask_30k/scenes-split-tmp \
    --output_scenes_dir /home/xingrui/publish/3D-Aware-VQA/superclevr-3D-question/output/ver_mask_30k/scenes_with_occlusion-tmp \
    --output_scene_file /home/xingrui/publish/3D-Aware-VQA/superclevr-3D-question/output/ver_mask_30k/superCLEVR_scenes_occlusion_tmp.json \
    --original_super_clevr_scene /home/xingrui/publish/3D-Aware-VQA/superclevr-3D-question/output/ver_mask_30k/last_9000.json