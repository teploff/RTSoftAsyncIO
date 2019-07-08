from collections import namedtuple
import requests
from time import time
from threading import Thread


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

    minimarkets_thread = Thread(target=launch_scoop, args=(SCRAPPERS[: 3], ))
    markets_thread = Thread(target=launch_scoop, args=(SCRAPPERS[3: 6], ))
    supermarkets_thread = Thread(target=launch_scoop, args=(SCRAPPERS[6: 9], ))
    hypermarkets_thread = Thread(target=launch_scoop, args=(SCRAPPERS[9: 12], ))
    threads = [minimarkets_thread, markets_thread, supermarkets_thread, hypermarkets_thread]

    start_time = time()
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time()

    elapsed_time = end_time - start_time

    print(f'Elapsed time = {elapsed_time} seconds')
