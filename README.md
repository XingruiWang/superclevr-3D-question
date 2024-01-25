# Super-CLEVR-3D Dataset
Footnote: This dataset is published as part of the NeurIPS'23 paper ["3D-Aware Visual Question Answering about Parts, Poses and Occlusions"](https://arxiv.org/abs/2310.17914). Please refer to the paper for a more detailed explanation and motivations of this dataset. The whole project of this paper can be found at [3D-Aware-VQA](https://github.com/XingruiWang/3D-Aware-VQA). 

## About
**Super-CLEVR-3D** is a visual question answering (VQA) dataset where the questions are about the explicit 3D configuration of the objects from images (i.e. **3D poses**, **parts**, and **occlusion**). It consists of objects from 5 categories: aeroplanes, buses, bicycles, cars and motorbikes. The rendered objects are from [CGParts](https://github.com/qliu24/render-3d-segmentation) dataset, with the same setting as [Super-CLEVR](https://arxiv.org/abs/2212.00259) dataset. 


## How to Download

| Name   | Download Link | Description                                                        |                                            
|--------|---------------------------|--------------------------------------------------------------------|
| Images |  [images.zip](https://www.cs.jhu.edu/~xwang378/share/Super-CLEVR-3D/images.zip) | There are 30k images in total. The first 20k are used for training, then 5k for validation and 5k for testing. |
| Annotations |  [scenes.json](https://www.cs.jhu.edu/~xwang378/share/Super-CLEVR-3D/scenes.json) | The corresponding annotation for each objects.|
| Questions | [questions.zip](https://www.cs.jhu.edu/~xwang378/share/Super-CLEVR-3D/questions.zip) |  Consist of 4 question files: `questions/superclevr_questions_obj_occlusion.json`, `questions/superclevr_questions_occlusion.json`, `questions/superclevr_questions_parts.json`, `questions/superclevr_questions_pose.json`.|

## Inspect the dataset

This [notebook](https://colab.research.google.com/drive/13ABF3164gSZFI35LELJ0DymmfyEL-5iK?usp=sharing) shows how you can load the questions and the image after you download the data.


## How to generate data by yourself

### 1. Generate Images and Scene Annotations

The scripts for image generation is in `scripts/render_images_3D.sh`. Please read this [documentation](https://github.com/XingruiWang/superclevr-3D-question/blob/main/image_generation/README.md) for more instructions.


### 2. Generate Questions

As introduced in the paper, we include three types of questions: pose, parts and occlusion.

1. Pose questions

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
```
2. Occlusion questions

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
