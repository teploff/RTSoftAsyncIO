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



def globus_scraper():
    print(globus_scraper.__name__, ' is launched...')
    sleep(3.25)
    print(globus_scraper.__name__, ' is over.')


def auchan_scraper():
    print(auchan_scraper.__name__, ' is launched...')
    sleep(3.5)
    print(auchan_scraper.__name__, ' is over.')


def metro_scraper():
    print(metro_scraper.__name__, ' is launched...')
    sleep(4)
    print(metro_scraper.__name__, ' is over.')


if __name__ == '__main__':
    start_time = time()

    dixy_scraper()
    pyaterochka_scraper()
    magnit_scraper()
    okey_scraper()
    spar_scraper()
    billa_scraper()
    perekrestok_scraper()
    lenta_scraper()
    karusel_scraper()
    globus_scraper()
    auchan_scraper()
    metro_scraper()

    end_time = time()

    elapsed_time = end_time - start_time

    print(f'Elapsed time = {elapsed_time}')
