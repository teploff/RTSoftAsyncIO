from time import sleep, time


def dixy_scraper():
    print(dixy_scraper.__name__, ' is launched...')
    sleep(1)
    print(dixy_scraper.__name__, ' is over.')


def pyaterochka_scraper():
    print(pyaterochka_scraper.__name__, ' is launched...')
    sleep(2)
    print(pyaterochka_scraper.__name__, ' is over.')


def magnit_scraper():
    print(magnit_scraper.__name__, ' is launched...')
    sleep(3)
    print(magnit_scraper.__name__, ' is over.')


if __name__ == '__main__':

    start_time = time()

    dixy_scraper()
    pyaterochka_scraper()
    magnit_scraper()

    end_time = time()

    elapsed_time = end_time - start_time

    print(f'Elapsed time = {elapsed_time}')
