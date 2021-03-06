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


def launch(scrapper_name, scrapper_url):
    print(f'{scrapper_name} scrapper is launched...')
    response = requests.get(scrapper_url)
    _ = response.content
    print(f'{scrapper_name} scrapper is over!')


if __name__ == '__main__':

    threads = [Thread(target=launch, args=(scrapper.name, scrapper.url, )) for scrapper in SCRAPPERS]

    start_time = time()

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time()

    elapsed_time = end_time - start_time

    print(f'Elapsed time = {elapsed_time} seconds')
