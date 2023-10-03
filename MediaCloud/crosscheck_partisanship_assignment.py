from MediaCloud.input.lit_reviewed_sources import sources, accepted_translations
import universal_functions as uf
import pandas as pd



def get_unique_papers(filename):
    data = uf.import_json(filename)['content']
    df = pd.DataFrame(data=data)
    try:
        newspapers =[x.lower() for x in list(df['media_name'].unique())]
    except KeyError:
        newspapers = []
    return newspapers

def count_accepted_paper_overlap(valid_lit:str, unique_newspapers:list)->int:
    count = 0
    for paper in sources[valid_lit]:
        if paper in unique_newspapers:
            count +=1
    return count

def count_nonaccepted_paper_overlap(valid_lit:str, unique_newspapers:list):

    cleaned_sources = {k:sources[k] for k in sources.keys() if valid_lit!=k}
    results = {}
    for k in cleaned_sources.keys():
        count = 0
        part = [j for j in accepted_translations.keys() if accepted_translations[j]==k][0]
        for paper in cleaned_sources[k]:
            if paper in unique_newspapers:
                count +=1
        results[part] = count
    return results

def export_results():
    path = "C:\\Users\\khahn\\Documents\\Github\\MA-Thesis_Fringe-to-Familiar\\Data_Collection\\Media_Cloud\\the_urls"
    url_files = uf.get_files_from_folder(path, 'json')
    results = []
    for file in url_files:
        p, date = uf.get_partisanship_date_from_urlfile(file)
        unique_papers = get_unique_papers(file)
        if p in accepted_translations.keys():
            accepted_lit = accepted_translations[p]
            outcome = count_nonaccepted_paper_overlap(accepted_lit, unique_papers)
            outcome['own'] = count_accepted_paper_overlap(accepted_lit, unique_papers)
            outcome['partisanship'] = p
            outcome['date'] = date
        else:
            outcome = count_nonaccepted_paper_overlap('', unique_papers)
            outcome['own'] = None
            outcome['partisanship'] = p
            outcome['date'] = date
        results.append(outcome)

    df = pd.DataFrame(data=results)
    df.to_csv('output/cross_check_results.csv')


# export_results()

# REVIEW results
df = pd.read_csv('output/cross_check_results.csv')

for p in uf.partisanships:
    sub_df = df.loc[df['partisanship']==p]
    print('')
print('')