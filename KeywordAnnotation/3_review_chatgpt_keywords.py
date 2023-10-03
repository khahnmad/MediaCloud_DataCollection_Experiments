import universal_functions as uf
from KeywordAnnotation.input import chatgpt_keywords as c
import re

# GLOBAL
RECON_DIR = uf.repo_loc / 'Reconstruction_Phase' # TODO: outdated
KEYWORDS = uf.import_json_content(RECON_DIR / 'Keyword_Identification/valid_keywords.json')

DATASETS = uf.get_files_from_folder(str(uf.repo_loc / 'Data_Collection/Final_Processing/Datasets'),'json') # TODO: outdated

def find_keyword(text,keyword):
    regex = fr'\b{keyword}\b'
    try:
        x = re.search(regex, text.lower())
    except re.error:
        x = None # '\\citizenship\\b'

    return x

def manually_remove_keywords():
    # Manually remove keywords that are obviously too broad to be applicable
    related= {k:[] for k in c.gpt.keys()}
    for k in c.gpt.keys():
        print(f"\n{k.upper()}")
        for word in c.gpt[k]:
            result = input(f"{word}: delete? y/n")
            if result != 'y':
                related[k].append(word)

    uf.content_json_export('expanded_keywords.json',related)


def annotate_article(keyword_vers:str, art_dict, bad_keywords ):
    if keyword_vers == 'gpt':
        keywords = c.gpt
    elif keyword_vers == 'og':
        keywords = KEYWORDS
    else:
        raise Exception('variable "keyword_vers" must be "gpt" or "og"')
    cats = {k:[] for k in keywords}
    for k in keywords.keys():
        for keyword in keywords[k]:
            if keyword in bad_keywords:
                continue
            match = find_keyword(art_dict['article_text'], keyword)
            if match:
                cats[k].append(keyword)
    return cats

def get_gpt_tags(gpt:dict,og:dict)->list:
    tags = []
    for k in gpt.keys():
        if len(gpt[k])>0 and len(og[k])==0:
            tags.append(k)
    return tags


def investigate_standalone_gpt_keywords():
    investigated = uf.import_json_content('investigated_gpt_keywords.json')
    for d in DATASETS[10:]:
        data = uf.import_json(d)['content']
        for elt in data:
            bad_keywords = [x for x in investigated.keys() if
                            len(investigated[x]) > 4 and sum(investigated[x]) / len(investigated[x]) <= (1 / 6)]
            elt['og_category'] = annotate_article('og',elt, bad_keywords)
            elt['gpt_category'] = annotate_article('gpt',elt, bad_keywords)

    # want to inspect occasions in which the gpt keywords tag an article that the og ones dont and see if that's a legitimate identification

            gpt_ids = get_gpt_tags(gpt=elt['gpt_category'], og=elt['og_category'])
            if len(gpt_ids)==0:
                continue
            # Check for false positive
            print(f"Article Text:\n{elt['article_text']}")
            for t in gpt_ids:
                print(f"GPT identified tags: {t}\n")
                for key in elt['gpt_category'][t]:
                    ft = input(f'{key}: False or True positive? f/t ')
                    if key not in investigated.keys():
                        investigated[key] = []
                    if ft == 't':
                        investigated[key].append(1)
                    else:
                        investigated[key].append(0)
            uf.content_json_export('investigated_gpt_keywords.json',investigated)

def fetch_remaining_keywords():
    investigated = uf.import_json_content('investigated_gpt_keywords.json')
    remaining = {k:{} for k in c.gpt.keys()}
    for k in c.gpt.keys():
        for keyword in c.gpt[k]:
            if keyword not in investigated:
                remaining[k][keyword]= []
    return remaining

def investigate_remaining_keywords():
    remaining = fetch_remaining_keywords()
    for d in DATASETS:
        data = uf.import_json(d)['content']
        for elt in data:

            for k in remaining.keys():
                for word in remaining[k].keys():
                    match = find_keyword(elt['article_text'],word)
                    if match:
                        remaining[k][word].append([])

                        for keyword in KEYWORDS[k]:
                            k_match = find_keyword(elt['article_text'],keyword)
                            if k_match:
                                remaining[k][word][-1].append(keyword)
    uf.content_json_export('remaining_keywords.json',remaining)



# ACTION
# Manually remove keywords: this process has already been run once
# manually_remove_keywords()

# Investigate gpt keywords when they appear unaccompanied by a valid keyword
# investigate_standalone_gpt_keywords()

# Investigate keywords that do not appear in the standalone investigation
# investigate_remaining_keywords()
