cd image_generation
echo $PWD >> /home/xingrui/packages/blender-2.79b-linux-glibc219-x86_64/2.79/python/lib/python3.5/site-packages/clevr.pth


CUDA_VISIBLE_DEVICES=3 ~/packages/blender-2.79b-linux-glibc219-x86_64/blender --background \
    --python super_restore_render_images.py -- \
    --start_idx 136000 \
    --num_images 549 \
    --use_gpu 1 \
    --shape_dir ~/data/CGPart \
    --model_dir data/save_models_1/ \
    --properties_json data/properties_cgpart.json \
    --margin 0.1 \
    --save_blendfiles 0 \
    --max_retries 150 \
    --width 640 \
    --height 480 \
    --output_image_dir ../output/ver_mask_new/images-split/ \
    --output_scene_dir ../output/ver_mask_new/scenes-split/ \
    --output_blend_dir ../output/ver_mask_new/blendfiles-split/ \
    --output_scene_file ../output/ver_mask_new/superCLEVR_scenes_split.json \
    --is_part 1 \
    --load_scene 1 \
    --clevr_scene_path ../output/ver_mask_new/superCLEVR_scenes_splitted.json
    # --clevr_scene_path ../output/ver_mask_new/superCLEVR_scenes_210k_splitted.json 

# 136549
    # --clevr_scene_path /home/zhuowan_intern/xingrui/super-clevr-gen/ver_mask/superCLEVR_scenes_5_tiny_0_rotation.json

    # --shape_color_co_dist_pth data/dist/shape_color_co_super.npz \

    # --clevr_scene_path ../output/superCLEVR_scenes_5.json

    # --color_dist_pth data/dist/color_dist.npz \
    # --mat_dist_pth data/dist/mat_dist.npz \
    # --shape_dist_pth data/dist/shape_dist.npz \


cd ..

