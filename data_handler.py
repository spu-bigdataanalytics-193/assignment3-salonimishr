import os
import glob
import shutil
import urllib3
import functools
import pandas as pd
import utils


DATA_SOURCE = 'http://stat-computing.org/dataexpo/2009'
DATA_DIR = os.path.join('data')


def download_handler(file_path, data_url):
    """
    downloads the data from stat computing website.
    """

    with urllib3.PoolManager().request('GET', data_url, preload_content=False) as r:
        if r.status == 200:
            with open(file_path, 'wb') as w:
                shutil.copyfileobj(r, w)
        else:
            print('internet connection error.')


def check_dataset():
    file_list = []
    for year in range(1987, 2009):
        file_path = '{}/raw_{}.csv.bz2'.format(DATA_DIR, year)
        file_list.append(file_path)

    if not any(map(os.path.exists, file_list)):
        return True
    else:
        return False


def download_dataset():
    """
    download all the years of flight data into data folder
    """
    if check_dataset():

        if not os.path.exists(DATA_DIR):
            os.mkdir(DATA_DIR)

        year_range = range(1987, 2009)
        for ind, year in enumerate(year_range):
            # vars
            data_url = '{}/{}.csv.bz2'.format(DATA_SOURCE, year)
            file_path = '{}/raw_{}.csv.bz2'.format(DATA_DIR, year)

            # download
            download_handler(file_path, data_url)
            
            # progress
            utils.progressbar(len(year_range), ind + 1, 'download status: ')
    else:
        print('data downloaded. you can skip this step or delete data folder to download again.')


def read_as_dataframe():
    """
    Read all files into one single dataframe.

    PS: this should work, unfortunately, my computer is slow to load all into one. 
    I didn't try this code, but if this works, you only need to loop for the rows.
    """
    par_func = functools.partial(pd.read_csv, compression='bz2', encoding='ISO-8859-1', memory_map=True)
    file_list = glob.glob(os.path.join(DATA_DIR, '*.csv.bz2'))
    df = pd.concat(map(par_func, file_list))

    return df