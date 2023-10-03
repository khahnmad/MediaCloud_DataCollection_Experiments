import universal_functions as uf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

def export_num_urls_by_month_partisanship():
    path = "C:\\Users\\khahn\\Documents\\Github\\MA-Thesis_Fringe-to-Familiar\\Data_Collection\\Media_Cloud\\the_urls"
    url_files = uf.get_files_from_folder(path, 'json')

    time_index = {'1-2016': 0, '2-2016': 1, '3-2016': 2, '4-2016': 3, '5-2016': 4, '6-2016': 5, '7-2016': 6, '8-2016': 7, '9-2016': 8, '10-2016': 9, '11-2016': 10, '12-2016': 11, '1-2017': 12, '2-2017': 13, '3-2017': 14, '4-2017': 15, '5-2017': 16, '6-2017': 17, '7-2017': 18, '8-2017': 19, '9-2017': 20, '10-2017': 21, '11-2017': 22, '12-2017': 23, '1-2018': 24, '2-2018': 25, '3-2018': 26, '4-2018': 27, '5-2018': 28, '6-2018': 29, '7-2018': 30, '8-2018': 31, '9-2018': 32, '10-2018': 33, '11-2018': 34, '12-2018': 35, '1-2019': 36, '2-2019': 37, '3-2019': 38, '4-2019': 39, '5-2019': 40, '6-2019': 41, '7-2019': 42, '8-2019': 43, '9-2019': 44, '10-2019': 45, '11-2019': 46, '12-2019': 47, '1-2020': 48, '2-2020': 49, '3-2020': 50, '4-2020': 51, '5-2020': 52, '6-2020': 53, '7-2020': 54, '8-2020': 55, '9-2020': 56, '10-2020': 57, '11-2020': 58, '12-2020': 59, '1-2021': 60, '2-2021': 61, '3-2021': 62, '4-2021': 63, '5-2021': 64, '6-2021': 65, '7-2021': 66, '8-2021': 67, '9-2021': 68, '10-2021': 69, '11-2021': 70, '12-2021': 71, '1-2022': 72, '2-2022': 73, '3-2022': 74, '4-2022': 75, '5-2022': 76, '6-2022': 77, '7-2022': 78, '8-2022': 79, '9-2022': 80, '10-2022': 81, '11-2022': 82, '12-2022': 83}
    outcome = {k:[None for i in range(84)] for k in uf.partisanships}
    for file in url_files:
        part, date = uf.get_partisanship_date_from_urlfile(file)
        time_id = time_index[date]

        size = len(uf.import_json(file)['content'])

        outcome[part][time_id] = size
    uf.content_json_export('num_urls_by_month_partisanship.json', outcome)

def generate_datetime_x():
    dates = []
    for yr in range(2016,2023):
        for m in range(1,13):
            dates.append(dt.datetime(year=yr, month=m, day=1))
    return dates


def plot_num_urls_by_month_partisanship():
    data = uf.import_json('num_urls_by_month_partisanship.json')['content']
    color_key = {'FarLeft': '#0017C7', 'Left': '#5A71E3', 'CenterLeft': '#B4CAFF', 'Center': '#7B8290',
                 'CenterRight': '#FFBAB2', 'Right': '#F25D59', 'FarRight': '#C60000'}
    # x = list(range(84))
    # xticks = ['1/2016', '2/2016', '3/2016', '4/2016', '5/2016', '6/2016', '7/2016', '8/2016', '9/2016', '10/2016', '11/2016', '12/2016', '1/2017', '2/2017', '3/2017', '4/2017', '5/2017', '6/2017', '7/2017', '8/2017', '9/2017', '10/2017', '11/2017', '12/2017', '1/2018', '2/2018', '3/2018', '4/2018', '5/2018', '6/2018', '7/2018', '8/2018', '9/2018', '10/2018', '11/2018', '12/2018', '1/2019', '2/2019', '3/2019', '4/2019', '5/2019', '6/2019', '7/2019', '8/2019', '9/2019', '10/2019', '11/2019', '12/2019', '1/2020', '2/2020', '3/2020', '4/2020', '5/2020', '6/2020', '7/2020', '8/2020', '9/2020', '10/2020', '11/2020', '12/2020', '1/2021', '2/2021', '3/2021', '4/2021', '5/2021', '6/2021', '7/2021', '8/2021', '9/2021', '10/2021', '11/2021', '12/2021', '1/2022', '2/2022', '3/2022', '4/2022', '5/2022', '6/2022', '7/2022', '8/2022', '9/2022', '10/2022', '11/2022', '12/2022']
    # x = ['1/2016', '3/2016', '5/2016', '7/2016', '9/2016', '11/2016', '1/2017', '3/2017', '5/2017', '7/2017', '9/2017', '11/2017', '1/2018', '3/2018', '5/2018', '7/2018', '9/2018', '11/2018', '1/2019', '3/2019', '5/2019', '7/2019', '9/2019', '11/2019', '1/2020', '3/2020', '5/2020', '7/2020', '9/2020', '11/2020', '1/2021', '3/2021', '5/2021', '7/2021', '9/2021', '11/2021', '1/2022', '3/2022', '5/2022', '7/2022', '9/2022', '11/2022']
    # ax = plt.subplot()
    # plt.locator_params(axis='x', nbins=4)
    # for p in data.keys():
    #     plt.plot(x, data[p],color=color_key[p], label=p)
    # plt.legend()
    # ax.set_xticks(x)
    # ax.set_xticklabels(xticks)
    # plt.xlabel('Date')
    # # plt.xticks(xticks)
    # plt.ylabel('Number of Articles Published')
    # plt.show()

    # alt
    # Text in the x-axis will be displayed in 'YYYY-mm' format.
    x = generate_datetime_x()
    ax = plt.subplot()
    for p in data.keys():
        ax.plot(x, data[p], color=color_key[p], label=p)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
    # Rotates and right-aligns the x labels so they don't crowd each other.
    # for label in ax.get_xticklabels(which='major'):
    #     label.set(rotation=30, horizontalalignment='right')
    plt.xlabel('Date')
    # plt.xticks(xticks)
    plt.legend()
    plt.ylabel('Number of Articles Published')
    plt.show()


# export_num_urls_by_month_partisanship() #Only needs to be run once, has already been run
plot_num_urls_by_month_partisanship()
