import glob
from typing import List
import csv
import sys
import pandas as pd
import json
import pickle

##################### VARIABLES #####################################################
partisanships = ['FarLeft', 'Left', 'CenterLeft', 'Center', 'CenterRight', 'Right', 'FarRight']

################ IMPORT FUNCTIONS ######################################
def manage_overflow():
    # Manages overflow from importing .csv files with lots of text data in one column
    maxInt = sys.maxsize
    while True:
        # decrease the maxInt value by factor 10
        # as long as the OverflowError occurs.
        try:
            csv.field_size_limit(maxInt)
            break
        except OverflowError:
            maxInt = int(maxInt / 10)


def import_csv(csv_file:str)->List[List]:
    # Given a file location, imports the data as a nested list, each row is a new list
    manage_overflow() # manage overflow from large lines
    nested_list = []  # initialize list
    with open(csv_file, newline='', encoding='utf-8') as csvfile:  # open csv file
        reader = csv.reader(csvfile, delimiter=',')
        try:
            for row in reader:
                nested_list.append(row)  # add each row of the csv file to a list
        except Exception as e:
            # NOTE: can't reproduce the error that I created this code for... not sure how to improve
            df = pd.read_csv(csv_file)
            columns = [list(df.columns)]
            nested_list = columns + df.values.tolist()
            for i in range(len(nested_list)):
                new_row = [str(x) for x in nested_list[i]]
                nested_list[i] = new_row
            print(f"CAUTION: {e} for file {csv_file}\n")
    return nested_list


def get_files_from_folder(folder_name:str, file_endings:str)->List[str]:
    return [x for x in glob.glob(folder_name + f"/*.{file_endings}")]


def import_json(file):
    with open(file, 'r') as j:
        content = json.loads(j.read())

    return content

def import_json_content(file:str):
    with open(file, 'r') as j:
        content = json.loads(j.read())['content']
    return content

def import_pkl_file(file):
    with open(file, "rb") as f:
        pkl_file = pickle.load(f)
        f.close()
    return pkl_file


################ EXPORT FUNCTIONS ######################################
def export_as_json(export_filename:str, output):
    if export_filename.endswith('.json') is not True:
        raise Exception(f"{export_filename} should be a .json file")
    try:
        with open(export_filename, "w") as outfile:
            outfile.write(output)
    except TypeError:
        response = input("'output' should be a str, not dict. Do you want to convert this using json.dumps()? Y/N")
        if response.lower()=='y':
            export_as_json(export_filename, json.dumps(output))

def content_json_export(export_name, data):
    content = json.dumps({'content': data})
    export_as_json(export_name, content)


def export_nested_list(csv_name:str, nested_list:List[List]):
    # Export a nested list as a csv with a row for each sublist
    with open(csv_name, 'w', newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        for row in nested_list:
            writer.writerow(row)

def export_as_pkl(export_name:str, content):
    with open(export_name, "wb") as f:
        pickle.dump(content, f)
        f.close()

###### ANALYTICS ##########################################
def get_partisanship_date_from_urlfile(filename:str)->tuple:
    conversion = {'CE19':'Center',
                  "CL19": 'CenterLeft',
                  'CO':'FarRight',
                  'CR19':'CenterRight',
                  'FR':'FarRight',
                  'HL':'FarLeft',
                  'HR':'FarRight',
                  'LL19':"Left",
                  'RR19':'Right'}
    part = filename.split('urls\\')[1].split('_urls')[0]
    date = filename.split('_urls_')[1].split('.json')[0]
    return conversion[part], date