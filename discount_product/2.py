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


def okey_scaper():
    print(okey_scaper.__name__, ' is launched...')
    sleep(4)
    print(okey_scaper.__name__, ' is over.')


def spar_scaper():
    print(spar_scaper.__name__, ' is launched...')
    sleep(5)
    print(spar_scaper.__name__, ' is over.')


def billa_scaper():
    print(billa_scaper.__name__, ' is launched...')
    sleep(6)
    print(billa_scaper.__name__, ' is over.')


if __name__ == '__main__':

    start_time = time()

    dixy_scraper()
    pyaterochka_scraper()
    magnit_scraper()
    okey_scaper()
    spar_scaper()
    billa_scaper()

    end_time = time()

    elapsed_time = end_time - start_time

    print(f'Elapsed time = {elapsed_time}')
