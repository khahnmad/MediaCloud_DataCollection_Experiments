import universal_functions as uf
from KeywordAnnotation.input import chatgpt_keywords as c
import json

# GLOBAL
VALID_KEYWORDS = uf.import_json_content(uf.repo_loc / 'Reconstruction_Phase' / 'Keyword_Identification/valid_keywords.json') # TODO: outdated

GPT_KEYWORDS = c.gpt
GPT_CONNOTATION = c.connotation
GPT_POS = c.pos
GPT_NEG = c.neg

DATASETS = uf.get_files_from_folder(str(uf.repo_loc / 'Data_Collection/Final_Processing/Datasets'),'json') # TODO: outdated

INVESTIGATED_GPT_KEYWORDS = uf.import_json_content('output/investigated_gpt_keywords.json')
REMAINING_GPT_KEYWORDS = uf.import_json_content('output/remaining_keywords.json')

def create_valid_expanded_list():
    valid_expanded = {k:VALID_KEYWORDS[k] for k in VALID_KEYWORDS.keys()}
    for k in INVESTIGATED_GPT_KEYWORDS.keys():
        if sum(INVESTIGATED_GPT_KEYWORDS[k]) / len(INVESTIGATED_GPT_KEYWORDS[k]) <= (1 / 6):
            # print(f'Bad: {k}: {INVESTIGATED_GPT_KEYWORDS[k]}')
            continue
        elif sum(INVESTIGATED_GPT_KEYWORDS[k]) / len(INVESTIGATED_GPT_KEYWORDS[k]) > (2 / 3):
            print(f'Good: {k}: {INVESTIGATED_GPT_KEYWORDS[k]}')
            # find in c.gpt
            cat = [kk for kk in GPT_KEYWORDS.keys() if k in GPT_KEYWORDS[kk]][0]
            valid_expanded[cat].append(k)
        else:
            # print(f'Unknown: {k}: {INVESTIGATED_GPT_KEYWORDS[k]}')
            continue

    for k in REMAINING_GPT_KEYWORDS.keys():
        for keyword in REMAINING_GPT_KEYWORDS[k]:
            num_times_identified = len(REMAINING_GPT_KEYWORDS[k][keyword])
            num_co_identified_keywords = len([x for x in REMAINING_GPT_KEYWORDS[k][keyword] if len(x)>0])
            if num_times_identified>0 and num_co_identified_keywords/num_times_identified > 2/3:
                print(f'Addding {keyword} with a ratio of {num_co_identified_keywords}/{num_times_identified}')
                valid_expanded[k].append(keyword)
            else:
                print(f"\nFailing to add {keyword} with a ratio of {num_co_identified_keywords}/{num_times_identified}")
    uf.export_as_json('Valid_expanded_keywords.json',json.dumps(valid_expanded))

def create_valid_expanded_list_w_connotation():
    keywords = uf.import_json('output/Valid_expanded_keywords.json')

    output = {k:{'positive':[],'negative':[],'neutral':[]} for k in keywords.keys()}


    for k in keywords.keys():
        for word in keywords[k]:
            if word in GPT_CONNOTATION[k]['positive'] or word in GPT_POS[k]:
                output[k]['positive'].append(word)
            elif word in GPT_CONNOTATION[k]['negative'] or word in GPT_NEG[k]:
                output[k]['negative'].append(word)
            else:
                output[k]['neutral'].append(word)
    uf.export_as_json('output/Valid_expanded_keywords_w_connotation.json',json.dumps(output))

create_valid_expanded_list_w_connotation()