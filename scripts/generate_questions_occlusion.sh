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


# /home/xingrui/vqa/super-clevr-gen/question_generation/super_clevr_templates
   # super_clevr_occlusion_new / super_clevr_object_occlusion / super_clevr_templates
   # superclevr_questions_occlusion_210k_no_red-4.json / superclevr_questions_obj_occlusion_210k_no_red-4.json / superclevr_questions_part_210k_no_red-4.json
   # super_clevr_occlusion
   # --verbose
   # --remove_redundant -1.0
      # --output_questions_file ../output/superclevr_questions_occlusion_0k55k_no_red.json \


      # --input_scene_file ../output/superCLEVR_scenes_100mb.json \

   # --output_questions_file ../output/ver_texture_same/questions/superCLEVR_questions_${START_IDX}.json \

cd -

