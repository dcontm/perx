from aiohttp import web
from . schemas import Item
import aiohttp_jinja2
import time
import threading
import datetime


q = []   # очередь задач
lock = True  # замок, блокирующий обработку новой задачи


def worker():
    global lock
    lock = False
    item = q[0]
    item.status = 'обрабатывается'
    item.start_date = datetime.datetime.now().strftime("%H:%M %d/%m")
    for _ in range(item.quantity):
        time.sleep(item.interval)
        item.current_value += item.delta
    q.pop(0)
    lock = True


@aiohttp_jinja2.template('queue.html')
async def queue(request):
    while True:
        if q and lock:
            thread = threading.Thread(target=worker)
            thread.start()
        else:
            break
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
    return web.HTTPFound('/')
