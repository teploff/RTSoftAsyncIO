from collections import namedtuple
import multiprocessing as mp
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

CPU_CORE_COUNTS = 4


def launch_scoop(scrappers):
    for scrapper in scrappers:
        print(f'{scrapper.name} scrapper is launched...')
        sleep(scrapper.delay)
        print(f'{scrapper.name} scrapper is over!')


if __name__ == '__main__':

    process = [mp.Process(target=launch_scoop, args=(SCRAPPERS[core * 3: core * 3 + 3], ))
               for core in range(CPU_CORE_COUNTS)]

    start_time = time()
    for proc in process:
        proc.start()

    for proc in process:
        proc.join()

    end_time = time()

    elapsed_time = end_time - start_time

    print(f'Elapsed time = {elapsed_time} seconds')
