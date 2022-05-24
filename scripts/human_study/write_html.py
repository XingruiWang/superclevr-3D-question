import random
import json
import pdb
# 50 users: 1000 questions
# 

random.seed(2022)

def write_html(output_pth, images, questions, n_per_row=2, template_pth='data/template.html'):
    with open(template_pth, 'r') as f:
        ALL_TMP = f.read()
    IMG_TMP = '            <td><img src=\"%s\" /> </td>\n'
    TXT_TMP = '            <td> (No-%d) %s </td>\n'
    NEW_ROW_TMP = '          <tr>\n%s          </tr>\n          <tr>\n%s          </tr>\n'
    to_write = ''
    to_write_img = ''
    to_write_txt = ''
    for i, (img, q) in enumerate(zip(images, questions)):
        n_row = i // n_per_row
        n_col = i % n_per_row
        to_write_img += IMG_TMP % img
        to_write_txt += TXT_TMP % (i+1, q)
        if n_col == n_per_row-1 or i==len(images)-1:
            to_write += NEW_ROW_TMP % (to_write_img, to_write_txt)
            to_write_img, to_write_txt = '', ''
    out = ALL_TMP % to_write
    with open(output_pth, 'w') as f:
        f.write(out)




def shuffle_ids(questions, output_pth='user_study.json'):
    all_question_ids = list(range(1,len(questions)))
    random.shuffle(all_question_ids)
    results = {'all_question_ids': all_question_ids, 'answers': [], 'questions': [], 'images': []}
    for qid in all_question_ids:
        img = questions[qid]['image_filename']
        q = questions[qid]['question']
        ans = questions[qid]['answer']
        results['images'].append(img)
        results['questions'].append(q)
        results['answers'].append(ans)
    with open(output_pth, 'w') as f:
        json.dump(results, f)

def generate_data(num_users, info_obj_pth, info_prt_pth, output_tmplate_pth):
    N_O = 10
    N_P = 10
    info_obj = json.load(open(info_obj_pth, 'r'))
    info_prt = json.load(open(info_prt_pth, 'r'))
    for user_id in range(num_users):
        ids_o = list(range(user_id * N_O, user_id * N_O+N_O))
        ids_p = list(range(user_id * N_P, user_id * N_P+N_P))
        questions, images = [], []
        for id in ids_o:
            questions.append(info_obj['questions'][id])
            images.append(info_obj['images'][id])
        for id in ids_p:
            questions.append(info_prt['questions'][id])
            images.append(info_prt['images'][id])
        output_pth = output_tmplate_pth % user_id
        
        # IMG_TMP = '<td><img src=\"/data/c/zhuowan/SuperClevr/super-clevr/output/ver_mask/images/%s\" /> </td>\n'
        images = ['./ver_mask/images/'+a for a in images]
        write_html(output_pth, images, questions, n_per_row=2, template_pth='data/template_with_instruction.html')

def main():
    ## debug: superCLEVR_questions_5_tiny.json
    obj_question_json_pth = 'data/ver_mask/questions/superCLEVR_questions_merged.json'
    prt_question_json_pth = 'data/ver_mask/questions/superCLEVR_questions_part_partquery.json'
    # prt_question_json_pth = '/data/c/zhuowan/SuperClevr/super-clevr/output/ver_mask/questions/superCLEVR_questions_5_tiny.json'
    info_obj_pth = 'data/obj_questions.json'
    info_prt_pth = 'data/prt_questions.json'
    output_tmplate_pth = 'output/user_%d.html'
    # obj_questions = json.load(open(obj_question_json_pth, 'r'))['questions']
    # prt_questions = json.load(open(prt_question_json_pth, 'r'))['questions']
    # shuffle_ids(obj_questions, info_obj_pth)
    # shuffle_ids(prt_questions, info_prt_pth)
    num_users = 20
    generate_data(num_users, info_obj_pth, info_prt_pth, output_tmplate_pth)

if __name__ == '__main__':
    main()


