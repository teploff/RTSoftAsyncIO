from collections import namedtuple
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
]


def launch(scrapper_name, scrapper_url):
    print(f'{scrapper_name} scrapper is launched...')
    response = requests.get(scrapper_url)
    _ = response.content
    print(f'{scrapper_name} scrapper is over!')


if __name__ == '__main__':

    start_time = time()

    for scrapper in SCRAPPERS:
        launch(scrapper.name, scrapper.url)

    end_time = time()

    elapsed_time = end_time - start_time

    print(f'Elapsed time = {elapsed_time} seconds')
