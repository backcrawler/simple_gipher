import tornado.web
from tornado.httpclient import AsyncHTTPClient


class MainView(tornado.web.RequestHandler):
    async def get(self):
        client = AsyncHTTPClient()
        ...


class SecondaryView(tornado.web.RequestHandler):
    async def get(self):
        ...

    async def delete(self):
        ...