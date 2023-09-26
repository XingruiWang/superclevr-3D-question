# SuperCLEVR-3D Dataset Generation

# Image Generation

The procedure of image generation is in `scripts/render_images_3D.sh`


# Computer the occlusion relationship

The original SuperCLEVR dataset doesn't record the occlusion part of each object, which will be uilizied to generate occlusion question. So we need to rerender the objects from the scene and computer the mask of occluded / visible part of each object.

1. Split the scene file



## Notes for super-CLEVR

1. To generate pose questions

```
cd question_generation

START_IDX=0
python generate_questions_pose.py \
   --input_scene_file ../output/ver_mask_new/superCLEVR_scenes_210k_occlusion.json \
   --scene_start_idx ${START_IDX} \
   --num_scenes 20000 \
   --instances_per_template 1 \
   --templates_per_image 10 \
   --metadata_file metadata_pose.json \
   --output_questions_file ../output/superclevr_questions_pose_no_red_2.json \
   --template_dir super_clevr_pose \
   --remove_redundant 1.0 \

cd..

```
2. To generate occlusion 

```
cd question_generation

START_IDX=0
python generate_questions.py \
   --input_scene_file ../output/ver_mask_new/superCLEVR_scenes_210k_occlusion.json \
   --scene_start_idx ${START_IDX} \
   --num_scenes 21000 \
   --instances_per_template 1 \
   --templates_per_image 10 \
   --metadata_file metadata_part_occlusion.json \
   --output_questions_file ../output/superclevr_questions_occlusion_210k.json \
   --template_dir super_clevr_occlusion_new \
   --remove_redundant 1.0

```
Set `template_dir=super_clevr_occlusion_new` if generating occlusion questions with parts; Set `template_dir=super_clevr_object_occlusion` if generating occlusion questions without parts; 
