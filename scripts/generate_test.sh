
cd question_generation
python generate_questions.py \
    --input_scene_file ../output/test_scenes.json \
    --scene_start_idx 0 \
    --num_scenes 1 \
    --instances_per_template 100 \
    --templates_per_image 100 \
    --metadata_file metadata_part.json \
    --template_dir super_clevr_templates \
    --remove_redundant 1.0 \
    --output_questions_file ../output/otest_remove.json

python generate_questions.py \
    --input_scene_file ../output/test_scenes.json \
    --scene_start_idx 0 \
    --num_scenes 1 \
    --instances_per_template 100 \
    --templates_per_image 100 \
    --metadata_file metadata_part.json \
    --template_dir super_clevr_templates \
    --output_questions_file ../output/otest_keep.json

cd -
