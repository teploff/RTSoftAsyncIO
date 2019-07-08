import asyncio
from collections import namedtuple
from time import time

import aiohttp


HOST = 'http://127.0.0.1:9000'
HANDLER = namedtuple('Handler', 'name url')
HANDLERS = [
    # minimarkets
    HANDLER('Minimarkets', HOST + '/minimarkets'),
    # markets
    HANDLER('Markets', HOST + '/markets'),
    # supermarkets
    HANDLER('Supermarkets', HOST + '/supermarkets'),
    # hypermarkets
    HANDLER('Hypermarkets', HOST + '/hypermarkets'),
]


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def launch(scrapper_name, scrapper_url):
    print(f'{scrapper_name} scrapper is launched...')
    async with aiohttp.ClientSession() as session:
        _ = await fetch(session, scrapper_url)
    print(f'{scrapper_name} scrapper is over!')


if __name__ == '__main__':

    start_time = time()

    handlers = [asyncio.ensure_future(launch(handler.name, handler.url)) for handler in HANDLERS]
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(asyncio.gather(*handlers))

    end_time = time()

    elapsed_time = end_time - start_time

    print(f'Elapsed time = {elapsed_time} seconds')
