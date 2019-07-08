import asyncio
from collections import namedtuple
import requests
from time import time

import aiohttp


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

    scrappers = [asyncio.ensure_future(launch(scrapper.name, scrapper.url)) for scrapper in SCRAPPERS]
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(asyncio.gather(*scrappers))

    end_time = time()

    elapsed_time = end_time - start_time

    print(f'Elapsed time = {elapsed_time} seconds')
