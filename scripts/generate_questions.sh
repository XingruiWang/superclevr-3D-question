# cd /home/zhuowan/zhuowan/SuperClevr/clevr-dataset-gen/question_generation
cd question_generation
# python generate_questions.py \
#     --input_scene_file /home/zhuowan/zhuowan/SuperClevr/CLEVR_v1.0/scenes/CLEVR_train_scenes.json \
#     --output_questions_file /home/zhuowan/zhuowan/SuperClevr/super-clevr/output/questions.json \
#     --scene_start_idx 0 \
#     --num_scenes 100

# python generate_questions.py \
#     --input_scene_file ../output/ver_texture/superCLEVR_scenes.json \
#     --scene_start_idx 0 \
#     --num_scenes 30000 \
#     --instances_per_template 1 \
#     --templates_per_image 10 \
#     --metadata_file metadata_part.json \
#     --template_dir super_clevr_templates \
#     --output_questions_file ../output/ver_mask/questions/superCLEVR_questions_part_partquery.json

START_IDX=25000
python generate_questions.py \
   --input_scene_file ../output/ver_mask/superCLEVR_scenes.json \
   --scene_start_idx ${START_IDX} \
   --num_scenes 5000 \
   --instances_per_template 1 \
   --templates_per_image 10 \
   --metadata_file metadata_part.json \
   --output_questions_file ../output/ver_mask/rd_n1/superCLEVR_questions_${START_IDX}.json \
   --template_dir CLEVR_1.0_templates \
   --remove_redundant -1.0

cd -

# CLEVR_1.0_templates
    # --input_scene_file ../output/CLEVR_scenes.json \
