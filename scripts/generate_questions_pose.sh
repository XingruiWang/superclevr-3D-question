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

cd -

