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

    thread_1 = Thread(target=launch_scoop, args=([SCRAPPERS[6], SCRAPPERS[11]], ))
    thread_2 = Thread(target=launch_scoop, args=([SCRAPPERS[8], SCRAPPERS[9]], ))
    thread_3 = Thread(target=launch_scoop, args=([SCRAPPERS[0], SCRAPPERS[3], SCRAPPERS[10]], ))
    thread_4 = Thread(target=launch_scoop, args=(
        [SCRAPPERS[1], SCRAPPERS[2], SCRAPPERS[3], SCRAPPERS[4], SCRAPPERS[5]],
    ))

    threads = [thread_1, thread_2, thread_3, thread_4]

    start_time = time()

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time()

    elapsed_time = end_time - start_time

    print(f'Elapsed time = {elapsed_time} seconds')
