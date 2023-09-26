cd image_generation

CUDA_VISIBLE_DEVICES=2 \
~/packages/blender-2.79b-linux-glibc219-x86_64/blender --background \
    --python super_restore_render_images_z_direction.py -- \
    --start_idx 0 \
    --num_images 100 \
    --use_gpu 1 \
    --shape_dir /home/xingrui/data/CGPart \
    --model_dir data/save_models_1/ \
    --properties_json data/properties_cgpart.json \
    --margin 0.1 \
    --save_blendfiles 0 \
    --max_retries 150 \
    --width 640 \
    --height 480 \
    --output_image_dir ../output/only_plane_in_sky_2/images/ \
    --output_scene_dir ../output/only_plane_in_sky_2/scenes/ \
    --output_blend_dir ../output/only_plane_in_sky_2/blendfiles \
    --output_scene_file ../output/only_plane_in_sky_2/superCLEVR_scenes.json \
    --is_part 1 \
    --load_scene 1 \
    # --clevr_scene_path /home/xingrui/publish/superclevr_3D_questions/output/3_direction/superCLEVR_scenes.json
    # --clevr_scene_path /home/xingrui/publish/superclevr_3D_questions/output/z_direction/superCLEVR_scenes.json
    # --clevr_scene_path ../output/ver_mask/superCLEVR_scenes.json 

    # --shape_color_co_dist_pth data/dist/shape_color_co_super.npz \

    # --clevr_scene_path ../output/superCLEVR_scenes_5.json

    # --color_dist_pth data/dist/color_dist.npz \
    # --mat_dist_pth data/dist/mat_dist.npz \
    # --shape_dist_pth data/dist/shape_dist.npz \


cd ..

