cd image_generation

CUDA_VISIBLE_DEVICES=5 \
~/packages/blender-2.79b-linux-glibc219-x86_64/blender --background \
    --python super_human_study.py -- \
    --start_idx 0 \
    --num_images 2 \
    --use_gpu 1 \
    --shape_dir ../../render-3d-segmentation/CGPart \
    --model_dir data/save_models_1/ \
    --properties_json data/properties_cgpart.json \
    --margin 0.1 \
    --save_blendfiles 1 \
    --max_retries 150 \
    --width 640 \
    --height 480 \
    --output_image_dir ../output/human_study/color_mat/images/ \
    --output_scene_dir ../output/human_study/color_mat/scenes/ \
    --output_blend_dir ../output/human_study/color_mat/blendfiles \
    --output_scene_file ../output/human_study/color_mat/superCLEVR_scenes.json \
    
    # --is_part 1 \
    # --load_scene 1 \
    # --clevr_scene_path ../output/ver_mask/superCLEVR_scenes.json 

cd ..

