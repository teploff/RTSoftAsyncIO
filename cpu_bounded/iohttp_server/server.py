from collections import namedtuple
from aiohttp import web


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


async def minimarkets(request):
    launch(HANDLERS[0].name, HANDLERS[0].dimension)
    return web.Response(text='ok')


async def markets(request):
    launch(HANDLERS[1].name, HANDLERS[1].dimension)
    return web.Response(text='ok')


async def supermarkets(request):
    launch(HANDLERS[2].name, HANDLERS[2].dimension)
    return web.Response(text='ok')


async def hypermarkets(request):
    launch(HANDLERS[3].name, HANDLERS[3].dimension)
    return web.Response(text='ok')

if __name__ == '__main__':
    app = web.Application()
    app.add_routes([
        web.get('/minimarkets', minimarkets),
        web.get('/markets', markets),
        web.get('/supermarkets', supermarkets),
        web.get('/hypermarkets', hypermarkets),

    ])
    web.run_app(app, host='127.0.0.1', port=9000)
