from aiohttp import web
from . schemas import Item
import aiohttp_jinja2
import datetime
import asyncio
from aiojobs.aiohttp import spawn

'''
Используем в качестве хранилища стандартный словарь,
а не collections.deque. Жертвуя скоростью выполнения,
получаем возможность передать номер позиции элемента методу .pop

'''
q = []


async def worker(item):
    item.status = 'обрабатывается'
    item.start_date = datetime.datetime.now().strftime("%H:%M %d/%m")
    for _ in range(item.quantity):
        await asyncio.sleep(item.interval)
        item.current_value += item.delta
    q.pop(q.index(item))


@aiohttp_jinja2.template('queue.html')
async def queue(request):
    return {'queue': q}


@aiohttp_jinja2.template('add_item.html')
async def add_item_get(request):
    return {}


@aiohttp_jinja2.template('add_item.html')
async def add_item_post(request):
    data = await request.post()

    item = Item(quantity=int(data['quantity']),
                delta=float(data['delta']),
                start_value=float(data['start_value']),
                current_value=float(data['start_value']),
                interval=float(data['interval'])
                )
    q.append(item)
    await spawn(request, worker(item))

    return web.HTTPFound('/')
