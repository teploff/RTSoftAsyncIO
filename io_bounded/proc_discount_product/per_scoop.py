from collections import namedtuple
import multiprocessing as mp
import requests
from time import time


HOST = 'http://127.0.0.1:9000'
SCRAPPER = namedtuple('Scraper', 'name url')
SCRAPPERS = [
    # minimarkets
    SCRAPPER('Dixy', HOST + '/dixy'),
    SCRAPPER('Pyaterochka', HOST + '/pyaterochka'),
    SCRAPPER('Magnit', HOST + '/magnit'),
    # markets
    SCRAPPER('Okey', HOST + '/okey'),
    SCRAPPER('Spar', HOST + '/spar'),
    SCRAPPER('Billa', HOST + '/billa'),
    # supermarkets
    SCRAPPER('Perekrestok', HOST + '/perekrestok'),
    SCRAPPER('Lenta', HOST + '/lenta'),
    SCRAPPER('Karusel', HOST + '/karusel'),
    # hypermarkets
    SCRAPPER('Globus', HOST + '/globus'),
    SCRAPPER('Auchan', HOST + '/auchan'),
    SCRAPPER('Metro', HOST + '/metro')
]


def launch_scoop(scrappers):
    for scrapper in scrappers:
        print(f'{scrapper.name} scrapper is launched...')
        response = requests.get(scrapper.url)
        _ = response.content
        print(f'{scrapper.name} scrapper is over!')


if __name__ == '__main__':

    minimarkets_process = mp.Process(target=launch_scoop, args=(SCRAPPERS[: 3], ))
    markets_process = mp.Process(target=launch_scoop, args=(SCRAPPERS[3: 6], ))
    supermarkets_process = mp.Process(target=launch_scoop, args=(SCRAPPERS[6: 9], ))
    hypermarkets_process = mp.Process(target=launch_scoop, args=(SCRAPPERS[9: 12], ))
    processes = [minimarkets_process, markets_process, supermarkets_process, hypermarkets_process]

    start_time = time()
    for proc in processes:
        proc.start()

    for proc in processes:
        proc.join()

    end_time = time()

    elapsed_time = end_time - start_time

    print(f'Elapsed time = {elapsed_time} seconds')
