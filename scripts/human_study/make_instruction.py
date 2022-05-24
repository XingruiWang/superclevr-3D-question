
import imageio
import pdb
from write_html import write_html
import glob
import os
import os.path as osp
from PIL import Image
import numpy as np
import json

def make_gif(filenames, output_pth):
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave(output_pth, images, duration=1)
    
def make_gifs(num):
    for i in range(num): #21
        filenames = []
        for t in range(12):
            img_pth = '/data/c/zhuowan/SuperClevr/super-clevr/output/human_study/visualize/'+str(i)+'_'+str(30*t)+'.png'
            filenames.append(img_pth)
        output_pth = '/data/c/zhuowan/SuperClevr/super-clevr/output/human_study/gifs/'+str(i)+'.gif'
        make_gif(filenames, output_pth)

def make_html():
    # output_pth = 'output/all_objects.html'
    output_pth = '/data/c/zhuowan/SuperClevr/super-clevr/output/human_study/all_objects.html'
    images = glob.glob('/data/c/zhuowan/SuperClevr/super-clevr/output/human_study/gifs/*.gif')
    images = ['./gifs/'+osp.basename(a) for a in images]
    # questions = [' ' for a in images]
    shapes = ['airliner', 'biplane', 'jet', 'fighter', 'utility', 'tandem', 'road', 'mountain', 'articulated', 'double', 'regular', 'school', 'truck', 'suv', 'minivan', 'sedan', 'wagon', 'chopper', 'scooter', 'cruiser', 'dirtbike']
    shape_name_map = {
      "suv": "suv",
      "wagon": "wagon",
      "minivan": "minivan",
      "sedan": "sedan",
      "truck": "truck",
      "addi": "regular car",
      "articulated": "articulated bus",
      "regular": "regular bus",
      "double": "double bus",
      "school": "school bus",
      "chopper": "chopper",
      "dirtbike": "dirtbike",
      "scooter": "scooter",
      "cruiser": "cruiser",
      "jet": "jet",
      "fighter": "fighter",
      "biplane": "biplane",
      "airliner": "airliner",
      "road": "road bike",
      "utility": "utility bike",
      "mountain": "mountain bike",
      "tandem": "tandem bike"
    }
    part_dict = json.load(open('../image_generation/data/save_models_1/part_dict.json', 'r'))
    
    questions = []
    for i in range(len(images)):
        shape = shapes[i]
        parts = part_dict[shape]
        parts = [post_process_part_name(p) for p in parts]
        questions.append(shape_name_map[shape]+'<p>'+', '.join(parts)+'</p>')
        
    shape_names = [shape_name_map[s] for s in shapes]
    print(', '.join(shape_names))
    write_html(output_pth, images, questions, n_per_row=4)
            
def center_crop(image, mask, resize=(240,180)):
    x1, x2 = 80, 560
    y1, y2 = 30, 390
    image = image.crop((x1, y1, x2, y2))
    mask = mask.crop((x1, y1, x2, y2))
    image = image.resize(resize, Image.ANTIALIAS)
    mask = mask.resize(resize, Image.NEAREST)
    return image, mask            

def post_process_visulize(num):
    for i in range(num): #21
        filenames = []
        for t in range(12):
            img_pth = '/data/c/zhuowan/SuperClevr/super-clevr/output/human_study/images/superCLEVR_new_%06d_%d.png' % (i, 30*t)
            img=Image.open(img_pth)
            # img=img.convert('RGB')
            mask_pth = '/data/c/zhuowan/SuperClevr/super-clevr/output/human_study/masks/'+str(i)+'_'+str(30*t)+'.png'
            anno=Image.open(mask_pth)
            img,anno = center_crop(img,anno)
            merged=(np.array(img)*0.2+np.array(anno)*0.8).astype(np.uint8)
            output_pth = '/data/c/zhuowan/SuperClevr/super-clevr/output/human_study/visualize/%d_%d.png' % (i, 30*t)
            out = Image.fromarray(merged)
            out.save(output_pth,"PNG")

def post_process_part_name(s):
    '''
    make door_right into right door (right, left, front, back, center, _s)
    '''
    if not isinstance(s, str):
        return s
    special_words = ['right', 'left', 'front', 'back', 'center', 'mid']
    s = s.split('_')
    if s[-1] == 's':
        s.pop(-1)
    while s[-1] in special_words:
        a = s.pop(-1)
        s.insert(0, a)
    s = ' '.join(s)
    return s


def main():
    # num = 21
    # post_process_visulize(num)
    # make_gifs(num)
    make_html()
    
if __name__ == '__main__':
    main()

    