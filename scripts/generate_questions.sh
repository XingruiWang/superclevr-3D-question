cd question_generation

#
# For all the setting
# 1. Object Occlusion 
#  --template_dir super_clevr_object_occlusion \
#  --output_questions_file superclevr_questions_obj_occlusion_210k_no_red-4.json

# 2. Part occlusion
#   --template_dir super_clevr_occlusion \
#   --output_questions_file superclevr_questions_occlusion.json

# 3. Part
#   --template_dir super_clevr_templates \
#   --output_questions_file superclevr_questions_part_210k_no_red-4.json


START_IDX=29997

python generate_questions.py \
   --input_scene_file ../output/ver_mask_30k_clean/superCLEVR_scenes_30k_occlusion.json \
   --scene_start_idx ${START_IDX} \
   --num_scenes 0 \
   --instances_per_template 1 \
   --templates_per_image 10 \
   --metadata_file metadata_part_occlusion.json \
   --template_dir super_clevr_object_occlusion \
   --output_questions_file superclevr_questions_obj_occlusion.json


# 4. Pose question (set `contain_pose`=True)

# python generate_questions.py \
#    --input_scene_file ../output/ver_mask_30k_clean/superCLEVR_scenes_30k_occlusion.json \
#    --scene_start_idx ${START_IDX} \
#    --num_scenes 0 \
#    --instances_per_template 2 \
#    --templates_per_image 8 \
#    --metadata_file metadata_part.json \
#    --output_questions_file ../output/ver_mask_30k/questions/superclevr_questions_pose.json \
#    --template_dir super_clevr_pose \
#    --remove_redundant 1.0 \
#    --contain_pose


