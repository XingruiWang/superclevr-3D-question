cd question_generation

START_IDX=27500
python generate_questions.py \
   --input_scene_file ../output/dist_texture_a1/superCLEVR_scenes.json \
   --scene_start_idx ${START_IDX} \
   --num_scenes 2500 \
   --instances_per_template 1 \
   --templates_per_image 10 \
   --metadata_file metadata_part.json \
   --output_questions_file ../output/dist_texture_a1/questions/superCLEVR_questions_${START_IDX}.json \
   --template_dir CLEVR_1.0_templates

   # --remove_redundant -1.0

cd -

