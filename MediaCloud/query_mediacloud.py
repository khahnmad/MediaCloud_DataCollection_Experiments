# TODO: link this within notes
# TODO: install mc_providers_main
from mc_providers_main.mc_providers_main.mc_providers.onlinenews import OnlineNewsMediaCloudProvider

import datetime as dt
import time

import os
from dotenv import load_dotenv

import universal_functions as uf


def file_has_been_run(file:str)->bool:
    # Check if the file already exists
    files = uf.get_files_from_folder('urls','json')
    match = [x for x in files if file in x]
    if len(match) > 0:
        return True
    return False


def fetch_stories_w_query(query, start_date, end_date, collection):
    load_dotenv()
    OLD_API_KEY = os.getenv("CONNECTION_STRING")

    provider = OnlineNewsMediaCloudProvider(api_key=OLD_API_KEY)
    stories = list(provider.all_items(query=query, start_date=start_date,end_date=end_date, collections=[collection]))
    return stories


def query_specific_range(collection,mon, yr):
    query = 'the'
    log_time = uf.import_csv('output/mc_query_time_log.csv')
    print(f"Collecting for {collection}, Month: {mon}, Year: {yr}")
    end_date = (dt.datetime(yr, mon+1, 1) - dt.timedelta(days=1)).day
    export_name = f'{collection}_urls_{mon}-{yr}.json'
    # if file_has_been_run(export_name):
    #     print("    - Already Run!\n")
    #     return
    a = time.time()
    exportable = []
    try:
        stories = fetch_stories_w_query(query=query,
                                        start_date=dt.datetime(year=yr, month=mon, day=1),
                                        end_date=dt.datetime(year=yr, month=mon, day=end_date),
                                        collection=collection)
    except Exception as e:

        print(f"    ERROR: {e}")
        return

    for elt in stories:
        exportable += elt

    print(f"    - found {len(exportable)} stories")
    if len(exportable)>0:
        uf.content_json_export(f"retry/{export_name}", exportable)
        b = time.time()
        log_time.append([b - a, len(exportable), dt.datetime.today()])
        print(f"    - took {b - a} seconds\n")
        uf.export_nested_list('mc_query_time_log.csv', log_time)
        return
    return


# COLLECTIONS
buzfeed_hyperpartisan_right = '31653028' # HR
us_farright = '214598068' # FR
conspiracies = '214609438' # CO
us_right_2019 = '200363049' # RR19
us_center_right_2019 = '200363062' # CR19
us_center_2019 = '200363050' # CE19
us_center_left_2019 = '200363048' #CL19
us_left_2019 = '200363061' # LL19
buzzfeed_hyperpartisan_left = '31653029' #HL

collections = {
                buzfeed_hyperpartisan_right :"HR",
               us_farright :"FR",
               conspiracies: "CO",
               us_right_2019: "RR19",
               us_center_right_2019: "CR19",
               us_center_2019: "CE19", # CE19 2022 12 is messed up
               us_center_left_2019: "CL19",
               us_left_2019:"LL19",
               buzzfeed_hyperpartisan_left:"HL"
    }


if __name__ == '__main__':
    # Combinations that I wanted to double check were run correctly
    # retry = [[conspiracies, 1, 2022],
    #          [conspiracies, 2, 2022],
    #          [conspiracies, 3, 2022],
    #          [conspiracies, 4, 2022],
    #          [us_farright,1,2022],
    #          [us_farright,2,2022],
    #          [us_farright,3,2022],
    #          [us_farright,4,2022],
    #          [buzzfeed_hyperpartisan_left,10,2021],
    #          [buzzfeed_hyperpartisan_left,2,2022],
    #          [buzzfeed_hyperpartisan_left,3,2022],
    #          [buzzfeed_hyperpartisan_left,4,2022],
    #          [buzfeed_hyperpartisan_right,1,2022],
    #          [buzfeed_hyperpartisan_right,2,2022],
    #          [buzfeed_hyperpartisan_right,3,2022],
    #          [us_right_2019,2,2022]]
    # for elt in retry:
    #     query_specific_range(collection=elt[0],mon=elt[1],yr=elt[2])


    query = 'the' # Query cannot be empty, so I chose a very common word, which I also briefly tested
    log_time = uf.import_csv('output/mc_query_time_log.csv')

    for k in collections.keys(): # Iterate through the collections
        for y in range(2016,2023): # Iterate through the years

            months = list(range(1,13))
            for m in range(len(months)): # Iterate through the months

                print(f"Collecting for {collections[k]}, Month: {months[m-1]}, Year: {y}")

                end_date = (dt.datetime(y, months[m], 1) - dt.timedelta(days=1)).day
                month = months[m-1]
                export_name = f'{collections[k]}_urls_{month}-{y}.json'

                if file_has_been_run(export_name):
                    print("    - Already Run!\n")
                    continue

                a = time.time()
                exportable = []
                try:
                    stories = fetch_stories_w_query(query=query,
                                                start_date=dt.datetime(year=y,month=month,day=1),
                                                end_date=dt.datetime(year=y,month=month,day=end_date),
                                                collection=k)
                except Exception as e:

                    print(f"    ERROR: {e}")
                    continue

                for elt in stories:
                    exportable += elt

                print(f"    - found {len(exportable)} stories")

                uf.content_json_export(f"the_urls/{export_name}",exportable)
                b = time.time()
                log_time.append([b-a, len(exportable), dt.datetime.today()])
                print(f"    - took {b-a} seconds\n")
                uf.export_nested_list('mc_query_time_log.csv',log_time)