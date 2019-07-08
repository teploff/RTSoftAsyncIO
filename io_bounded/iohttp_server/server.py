from aiohttp import web
import asyncio


async def dixy(request):
    await asyncio.sleep(0.25)
    return web.Response(text='ok')


async def pyaterochka(request):
    await asyncio.sleep(0.5)
    return web.Response(text='ok')


async def magnit(request):
    await asyncio.sleep(1)
    return web.Response(text='ok')


async def okey(request):
    await asyncio.sleep(1.25)
    return web.Response(text='ok')


async def spar(request):
    await asyncio.sleep(1.5)
    return web.Response(text='ok')


async def billa(request):
    await asyncio.sleep(2)
    return web.Response(text='ok')


async def perekrestok(request):
    await asyncio.sleep(2.25)
    return web.Response(text='ok')


async def lenta(request):
    await asyncio.sleep(2.5)
    return web.Response(text='ok')


async def karusel(request):
    await asyncio.sleep(3)
    return web.Response(text='ok')


async def globus(request):
    await asyncio.sleep(3.25)
    return web.Response(text='ok')


async def auchan(request):
    await asyncio.sleep(3.5)
    return web.Response(text='ok')


async def metro(request):
    await asyncio.sleep(4)
    return web.Response(text='ok')


if __name__ == '__main__':
    app = web.Application()
    app.add_routes([
        web.get('/dixy', dixy),
        web.get('/pyaterochka', pyaterochka),
        web.get('/magnit', magnit),

        web.get('/okey', okey),
        web.get('/spar', spar),
        web.get('/billa', billa),

        web.get('/perekrestok', perekrestok),
        web.get('/lenta', lenta),
        web.get('/karusel', karusel),

        web.get('/globus', globus),
        web.get('/auchan', auchan),
        web.get('/metro', metro),
    ])
    web.run_app(app, host='127.0.0.1', port=9000)
