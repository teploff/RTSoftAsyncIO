from collections import namedtuple
from time import sleep, time

SCRAPPER = namedtuple('Scraper', 'name delay')

SCRAPPERS = [
    # minimarkets
    SCRAPPER('dixy', 0.25),
    SCRAPPER('pyaterochka', 0.5),
    SCRAPPER('magnit', 1),
    # markets
    SCRAPPER('okey', 1.25),
    SCRAPPER('spar', 1.5),
    SCRAPPER('billa', 2),
    # supermarkets
    SCRAPPER('perekrestok', 2.25),
    SCRAPPER('lenta', 2.5),
    SCRAPPER('karusel', 3),
    # hypermarkets
    SCRAPPER('globus', 3.25),
    SCRAPPER('auchan', 3.5),
    SCRAPPER('metro', 4)
]


def launch(scrapper_name, scrapper_delay):
    print(f'{scrapper_name} scrapper is launched...')
    sleep(scrapper_delay)
    print(f'{scrapper_name} scrapper is over!')


if __name__ == '__main__':

    start_time = time()

    for scrapper in SCRAPPERS:
        launch(scrapper.name, scrapper.delay)

    end_time = time()

    elapsed_time = end_time - start_time

    print(f'Elapsed time = {elapsed_time} seconds')
