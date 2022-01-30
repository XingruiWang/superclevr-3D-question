
cd question_generation
python generate_questions.py \
    --input_scene_file ../output/test_scenes.json \
    --scene_start_idx 0 \
    --num_scenes 1 \
    --instances_per_template 1000 \
    --templates_per_image 1000 \
    --metadata_file metadata_part.json \
    --template_dir super_clevr_templates \
    --remove_redundant 1.0 \
    --verbose \
    --output_questions_file ../output/otest_remove.json


cd -
