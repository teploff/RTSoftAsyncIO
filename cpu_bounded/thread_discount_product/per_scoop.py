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


def launch_scoop(handlers):
    for handler in handlers:
        print(f'{handler.name} handler is launched...')
        fact = 1
        for n in range(1, handler.dimension + 1):
            fact *= n
        print(f'{handler.name} handler is over!')


if __name__ == '__main__':

    thread_1 = Thread(target=launch_scoop, args=(HANDLERS[: 2], ))
    thread_2 = Thread(target=launch_scoop, args=(HANDLERS[2: 4], ))
    threads = [thread_1, thread_2]

    start_time = time()
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time()

    elapsed_time = end_time - start_time

    print(f'Elapsed time = {elapsed_time} seconds')
