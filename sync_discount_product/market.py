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
