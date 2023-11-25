# Super-CLEVR-3D Dataset Generation

The implementation of Super-CLEVR-3D dataset. This dataset is published in NeurIPS 2023 paper [3D-Aware Visual Question Answering about Parts, Poses and Occlusions](https://arxiv.org/abs/2310.17914). The implementaion of model is in [3D-Aware-VQA](https://github.com/XingruiWang/3D-Aware-VQA). 

The code is still updating, and the dataset download link is coming soon.

# Image Generation

The procedure of image generation is in `scripts/render_images_3D.sh`. Please read this documentation for more instructions.



## 3D-Aware Question Generation

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
