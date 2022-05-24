import json
import pdb
from PIL import Image

def write_label_studio_html():
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
    
    html = ''
    for i in range(len(shapes)):
        shape = shapes[i]
        parts = part_dict[shape]
        parts = [post_process_part_name(p) for p in parts]
        html += '         <Choice value=\"%s\">\n' % shape_name_map[shape]
        for part in parts:
            html += '           <Choice value=\"%s\"/>\n' % (shape_name_map[shape]+': '+part)
        html += '         </Choice>\n'
        
    with open('output/labelstudio_template.html', 'w') as f:
        f.write(html)
        
    
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


def write_csv():
    f = open('output/labelstudio_3000.csv', 'w')
    f.write('image,question\n')
    
    info_obj_pth = 'data/obj_questions.json'
    info_prt_pth = 'data/prt_questions.json'
    # obj_questions = json.load(open(obj_question_json_pth, 'r'))['questions']
    # prt_questions = json.load(open(prt_question_json_pth, 'r'))['questions']
    # shuffle_ids(obj_questions, info_obj_pth)
    # shuffle_ids(prt_questions, info_prt_pth)
    num_examples = 1000

    N_O = 2
    N_P = 1
    info_obj = json.load(open(info_obj_pth, 'r'))
    info_prt = json.load(open(info_prt_pth, 'r'))
    for num in range(num_examples):
        for no in range(N_O):
            id = N_O*num + no
            f.write('https://www.cs.jhu.edu/~zhuowan/zhuowan/SuperCLEVR/human_study/output/ver_mask/images/'+info_obj['images'][id]+','+fix_question(info_obj['questions'][id])+'\n')
        for np in range(N_P):
            id = N_P*num + np
            f.write('https://www.cs.jhu.edu/~zhuowan/zhuowan/SuperCLEVR/human_study/output/ver_mask/images/'+info_prt['images'][id]+','+fix_question(info_prt['questions'][id])+'\n')
    f.close()

def fix_question(q):
    return q.replace('buss', 'buses')

def center_crop(image, resize=(240,180)):
    x1, x2 = 80, 560
    y1, y2 = 30, 390
    image = image.crop((x1, y1, x2, y2))
    image = image.resize(resize, Image.ANTIALIAS)
    return image 

def crop_color_mat_image():
    for i in range(8): 
        for t in range(2):
            img_pth = '/data/c/zhuowan/SuperClevr/super-clevr/output/human_study/color_mat/images/superCLEVR_new_%06d_%d.png' % (i, t)
            img=Image.open(img_pth)
            img = center_crop(img)
            output_pth = '/data/c/zhuowan/SuperClevr/super-clevr/output/human_study/color_mat/output/%d_%d.png' % (i, t)
            # out = Image.fromarray(img)
            img.save(output_pth,"PNG")
            
if __name__ == '__main__':
    # write_label_studio_html()
    # write_csv()
    crop_color_mat_image()