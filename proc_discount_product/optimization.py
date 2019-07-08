from collections import namedtuple
import multiprocessing as mp
from time import sleep, time

SCRAPPER = namedtuple('Scraper', 'name delay')

SCRAPPERS = [
    # minimarkets
    SCRAPPER('dixy', 0.25),        # 0
    SCRAPPER('pyaterochka', 0.5),  # 1
    SCRAPPER('magnit', 1),         # 2
    # markets
    SCRAPPER('okey', 1.25),        # 3
    SCRAPPER('spar', 1.5),         # 4
    SCRAPPER('billa', 2),          # 5
    # supermarkets
    SCRAPPER('perekrestok', 2.25), # 6
    SCRAPPER('lenta', 2.5),        # 7
    SCRAPPER('karusel', 3),        # 8
    # hypermarkets
    SCRAPPER('globus', 3.25),      # 9
    SCRAPPER('auchan', 3.5),       # 10
    SCRAPPER('metro', 4)           # 11
]

CPU_CORE_COUNTS = 4


def launch_scoop(scrappers):
    for scrapper in scrappers:
        print(f'{scrapper.name} scrapper is launched...')
        sleep(scrapper.delay)
        print(f'{scrapper.name} scrapper is over!')


if __name__ == '__main__':

    process_1 = mp.Process(target=launch_scoop, args=(
        [SCRAPPERS[6], SCRAPPERS[11]],
    ))
    process_2 = mp.Process(target=launch_scoop, args=(
        [SCRAPPERS[8], SCRAPPERS[9]],
    ))
    process_3 = mp.Process(target=launch_scoop, args=(
        [SCRAPPERS[0], SCRAPPERS[3], SCRAPPERS[10]],
    ))
    process_4 = mp.Process(target=launch_scoop, args=(
        [SCRAPPERS[1], SCRAPPERS[2], SCRAPPERS[3], SCRAPPERS[4], SCRAPPERS[5]],
    ))

    process = [process_1, process_2, process_3, process_4]

    start_time = time()
    for proc in process:
        proc.start()

    for proc in process:
        proc.join()

    end_time = time()

    elapsed_time = end_time - start_time

    print(f'Elapsed time = {elapsed_time} seconds')
