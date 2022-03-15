cd image_generation

CUDA_VISIBLE_DEVICES=7 \
~/packages/blender-2.79b-linux-glibc219-x86_64/blender --background \
    --python super_restore_render_images.py -- \
    --start_idx 7181 \
    --num_images 1 \
    --use_gpu 1 \
    --shape_dir ../../render-3d-segmentation/CGPart \
    --model_dir data/save_models_1/ \
    --properties_json data/properties_cgpart.json \
    --margin 0.1 \
    --save_blendfiles 1 \
    --max_retries 150 \
    --width 640 \
    --height 480 \
    --output_image_dir ../output/ver2/images/ \
    --output_scene_dir ../output/ver2/scenes/ \
    --output_blend_dir ../output/ver2/blendfiles \
    --output_scene_file ../output/ver2/superCLEVR_scenes.json \
   --clevr_scene_path ../output/ver_texture/superCLEVR_scenes.json

    # --output_image_dir ../output/ver_texture/images/ \
    # --output_scene_dir ../output/ver_texture/scenes/ \
    # --output_blend_dir ../output/ver_texture/blendfiles \
    # --output_scene_file ../output/ver_texture/superCLEVR_scenes.json \




#    --clevr_scene_path ../output/superCLEVR_scenes.json

cd ..

