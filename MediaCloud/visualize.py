#TODO: install numpy
# TODO:
import universal_functions as uf
import matplotlib.pyplot as plt
import dateutil.parser
import ast
import numpy as np

URL_FILES = uf.get_files_from_folder(f"..\\urls",'json')

def get_collection(filename):
    return filename.split('urls\\')[1].split('_urls')[0]

def get_time(filename):
    time = filename.split('_urls_')[1].split('.json')[0]
    month = time.split('-')[0]
    year = time.split('-')[1]
    return month, year

def collect_newspaper_per_collection():
    try:
        data = uf.import_csv('newspapers_per_collection.csv')
        y = [sum(ast.literal_eval(i)) for i in data[0]]
        x = data[1]
    except FileNotFoundError:
        summary = {}
        for file in URL_FILES:
            c = get_collection(file)
            data = uf.import_json_content(file)
            if c not in summary.keys():
                summary[c] = []

            for elt in data:
                if elt['media_id'] not in summary[c]:
                    summary[c].append(elt['media_id'])
        uf.export_nested_list('newspapers_per_collection.cav',[ list(summary.values()), list(summary.keys())])
        y = list(summary.keys())
        x = [sum(summary[k]) for k in summary.keys()]
    return x,y


def collect_pub_times_by(f:str):
    if f=='day_of_week':
        dates = uf.import_pkl_file('overall_dates.pkl')
        days = [d.weekday() for d in dates]
        X, Y = np.unique(days, return_counts=True)
        return X, Y
    if f=='time_of_day':
        dates = uf.import_pkl_file('overall_dates.pkl')
        times = [d.replace(year=2000,day=1,month=1) for d in dates]
        X, Y = np.unique(times, return_counts=True)
        return X, Y
    if f=='overall':
        try:
            dates = uf.import_pkl_file('overall_dates.pkl')
        except FileNotFoundError:
            dates = []
            for file in URL_FILES:
                data = uf.import_json_content(file)
                for elt in data:
                    if elt['publish_date'] == None:
                        continue
                    date= dateutil.parser.parse(elt['publish_date'])
                    dates.append(date)

            uf.export_as_pkl('overall_dates.pkl',dates)

        X, Y = np.unique(dates, return_counts=True)
        return X,Y



def plot_unique_newspapers_per_collection():
    x,y = collect_newspaper_per_collection()

    plt.bar(x,y)
    plt.xlabel('Collections')
    plt.ylabel('Number of Unique Newspapers (in thousands)')
    plt.title('Number of Unique Newspapers in each Media Cloud collection')
    plt.show()


def plot_pub_times_by(freq:str):
    x,y = collect_pub_times_by(freq)

    plt.plot(x,y)
    plt.xlabel(freq)
    plt.ylabel('Number of Articles published')
    plt.title(f'Publication times by {freq} for all articles')
    plt.show()

def plot_articles_by_partisanship():
    try:
        output = uf.import_json('articles_by_partisanship.json')['content']
    except FileNotFoundError:
        output = {'FarLeft': 0, 'Left': 0, 'CenterLeft': 0, 'Center': 0, 'CenterRight': 0, 'Right': 0, 'FarRight': 0}
        collection_conversion = {'CE19':'Center',
                                 'CL19':'CenterLeft',
                                 'CO':'FarRight',
                                 "CR19":'CenterRight',
                                 'FR':'FarRight',
                                 'HL':"FarLeft",
                                 'HR':'FarRight',
                                 'LL19':'Left',
                                 'RR19':'Right'}
        for url in URL_FILES:
            content = uf.import_json_content(url)
            collection = get_collection(url)
            part = collection_conversion[collection]
            output[part] += len(content)
        uf.content_json_export('articles_by_partisanship.json',output)

    x = list(output.keys())
    y = list(output.values())
    plt.bar(x,y)
    plt.xlabel('Partisanship')
    plt.ylabel('Number of Articles')
    plt.title("Number of Articles by Partisanship")
    plt.show()


def article_count_by_yr_partisanship():
    try:
        output = uf.import_json('articles_by_partisanship_year.json')['content']
    except FileNotFoundError:
        output = {'FarLeft': {2016: 0, 2017: 0, 2018: 0, 2019: 0, 2020: 0, 2021: 0, 2022: 0},
                  'Left': {2016: 0, 2017: 0, 2018: 0, 2019: 0, 2020: 0, 2021: 0, 2022: 0},
                  'CenterLeft': {2016: 0, 2017: 0, 2018: 0, 2019: 0, 2020: 0, 2021: 0, 2022: 0},
                  'Center': {2016: 0, 2017: 0, 2018: 0, 2019: 0, 2020: 0, 2021: 0, 2022: 0},
                  'CenterRight': {2016: 0, 2017: 0, 2018: 0, 2019: 0, 2020: 0, 2021: 0, 2022: 0},
                  'Right': {2016: 0, 2017: 0, 2018: 0, 2019: 0, 2020: 0, 2021: 0, 2022: 0},
                  'FarRight': {2016: 0, 2017: 0, 2018: 0, 2019: 0, 2020: 0, 2021: 0, 2022: 0}}
        collection_conversion = {'CE19': 'Center',
                                 'CL19': 'CenterLeft',
                                 'CO': 'FarRight',
                                 "CR19": 'CenterRight',
                                 'FR': 'FarRight',
                                 'HL': "FarLeft",
                                 'HR': 'FarRight',
                                 'LL19': 'Left',
                                 'RR19': 'Right'}
        for url in URL_FILES:
            content = uf.import_json_content(url)
            collection = get_collection(url)
            m, year = get_time(url)
            part = collection_conversion[collection]
            output[part][int(year)] += len(content)
        uf.content_json_export('articles_by_partisanship_year.json', output)

    for part in output.keys():
        x = list(output[part].keys())
        y = list(output[part].values())
        plt.plot(x, y, label=part)

    plt.xlabel('Partisanship')
    plt.ylabel('Number of Articles')
    plt.title("Number of Articles by Partisanship and Year")
    plt.legend()
    plt.show()

# unique newspapers per medaia cloud collection
plot_unique_newspapers_per_collection() # Ran

# publication times for all articles by frequency
plot_pub_times_by(freq='overall') # Ran
plot_pub_times_by(freq='time_of_day') # Ran
plot_pub_times_by(freq='day_of_week') # Ran


# x axis partisanship, y axis article count
plot_articles_by_partisanship()

# x axis year y axis count, breakdown by partisanship
article_count_by_yr_partisanship()
# English to not english bar plot
