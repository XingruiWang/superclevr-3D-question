# cd /home/zhuowan/zhuowan/SuperClevr/clevr-dataset-gen/question_generation
cd question_generation

## (for debug purpose) generate questions based on orinal CLEVR scenes
# python generate_questions.py \
#     --input_scene_file /home/zhuowan/zhuowan/SuperClevr/CLEVR_v1.0/scenes/CLEVR_train_scenes.json \
#     --output_questions_file output/sample_questions.json \
#     --scene_start_idx 0 \
#     --num_scenes 10

# Generate questions with part template for super-CLEVR
START_IDX=0

python generate_questions.py \
   --input_scene_file ../output/superCLEVR_scenes_100mb.json \
   --scene_start_idx ${START_IDX} \
   --num_scenes 5 \
   --instances_per_template 10 \
   --templates_per_image 10 \
   --remove_redundant 1.0 \
   --metadata_file metadata_part.json \
   --template_dir CLEVR_1.0_templates \
   --output_questions_file ../output/align/superCLEVR_questions_nrd_${START_IDX}.json

# Generate questions with original CLEVR template for super-CLEVR
python generate_questions.py \
    --input_scene_file ../output/superCLEVR_scenes_100mb.json \
    --scene_start_idx 0 \
    --num_scenes 5 \
    --instances_per_template 1 \
    --templates_per_image 10 \
    --metadata_file metadata_part.json \
    --output_questions_file ../output/align/superCLEVR_questions_${START_IDX}.json \
    --template_dir CLEVR_1.0_templates

#
# Align to the non-redundant examples 
python align_removed.py \
   --kept-file ../output/align/superCLEVR_questions_${START_IDX}.json \
   --new-file ../output/align/superCLEVR_questions_nrd_${START_IDX}.json \
   --out-file ../output/align/superCLEVR_questions_aligned_${START_IDX}.json

echo "wrote output to ../output/superCLEVR_questions_part_aligned.json"

cd -

# CLEVR_1.0_templates
    # --input_scene_file ../output/CLEVR_scenes.json \
