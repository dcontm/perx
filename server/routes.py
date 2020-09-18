from . views import queue, add_item_get, add_item_post


def setup_routes(app):
    app.router.add_get('/', queue)
    app.router.add_get('/add_item', add_item_get)
    app.router.add_post('/add_item', add_item_post)
