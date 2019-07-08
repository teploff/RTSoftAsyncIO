from collections import namedtuple
from time import time
from threading import Thread


HANDLER = namedtuple('Handler', 'name dimension')
HANDLERS = [
    # minimarkets
    HANDLER('Minimarkets', 200000),
    # markets
    HANDLER('Markets', 200000),
    # supermarkets
    HANDLER('Supermarkets', 200000),
    # hypermarkets
    HANDLER('Hypermarkets', 200000),
]


def launch(handler_name, handler_dimension):
    print(f'{handler_name} handler is launched...')
    fact = 1
    for n in range(1, handler_dimension + 1):
        fact *= n
    print(f'{handler_name} handler is over!')

    return fact


if __name__ == '__main__':

    threads = [Thread(target=launch, args=(handler.name, handler.dimension, )) for handler in HANDLERS]

    start_time = time()

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time()

    elapsed_time = end_time - start_time

    print(f'Elapsed time = {elapsed_time} seconds')
