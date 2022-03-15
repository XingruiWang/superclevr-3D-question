import json
import copy

def main():
    res = None
    paths = ['output/ver_mask/rd_n1/superCLEVR_questions_'+str(i*5000)+'.json' for i in range(6)]
    for pth in paths:
        print(pth)
        with open(pth, 'r') as f:
            if res is None:
                res = json.load(f)
            else:
                res['questions'].extend(json.load(f)['questions'])
    
    _res = res
    # _res = {'info': res['info'], 'questions': []}
    # for q in res['questions']:
    #     if q['image_index'] != 7181:
    #         _res['questions'].append(q)
            
    with open('output/ver_mask/rd_n1/superCLEVR_questions_merged.json', 'w') as f:
        json.dump(_res, f)

if __name__ == '__main__':
    main()