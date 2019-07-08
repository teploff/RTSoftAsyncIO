from collections import namedtuple
from time import time


HOST = 'http://127.0.0.1:9000'
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

    start_time = time()

    for handler in HANDLERS:
        launch(handler.name, handler.dimension)

    end_time = time()

    elapsed_time = end_time - start_time

    print(f'Elapsed time = {elapsed_time} seconds')
