import json
from collections import Counter

obj_question_types = {'query': ['query_shape', 'query_size', 'query_color', 'query_material'],
                 'equal': ['equal_shape', 'equal_size', 'equal_color', 'equal_material'],
                 'compare': ['equal_integer', 'greater_than', 'less_than'],
                 'count': ['count'],
                 'exist': ['exist']}
prt_question_types = {'query': ['query_shape', 'query_color', 'query_material'],
                 'partquery': ['partquery_partname', 'partquery_color', 'partquery_material']}

predictions = json.load(open('human_results.json', 'r'))
# predictions[0]:
# {'human': 'metal', # human answer
#  'type': 'query_material',
#  'answer': 'metal', #groundtruth
#  'is_part': 'prt',
#  'question': 'What is the material of the blue thing that has a yellow tail light?',
#  'image': 'superCLEVR_new_014740'}

      
for question_types, is_part in zip([obj_question_types, prt_question_types], ['obj', 'prt']):
    counter = {}
    for st in question_types:
        for t in question_types[st]: 
            counter[t] = {'human':0, 'no_idea':0, 'answer':0}
    counter['all'] = {'human':0, 'no_idea':0, 'answer':0}

    for p in predictions:
        if p['is_part'] != is_part:
            continue
        k = 'human'
        if p[k] == p['answer']:
            counter[p['type']][k] += 1
            counter['all'][k] += 1
        elif p[k] == '-1':
            counter[p['type']]['no_idea'] += 1
            counter['all']['no_idea'] += 1
        # else:
        #     print(p[k], p['answer'])
        counter[p['type']]['answer'] += 1
        counter['all']['answer'] += 1    

    for t in counter:
        correct_rate = float(counter[t]['human'])/counter[t]['answer']*100
        noidea_rate = float(counter[t]['no_idea'])/counter[t]['answer']*100
        print('%20s, %6.2f, \t %6.2f, \t %d, \t %d, \t %d' % (t, correct_rate, noidea_rate, counter[t]['human'], counter[t]['no_idea'], counter[t]['answer']))

    print('\n\n')