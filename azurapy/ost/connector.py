from typing import Dict
from .models.nowplaying import NowPlaying
import httpx


class Connector:

    headers: Dict[str, str]

    def __init__(self, client):
        self.headers = {'Authorization': f'Bearer {client.key}'}
        self.client = httpx.Client(headers=self.headers)
        self.domain = client.domain



    # def proxy(cls):
    #     def inner(self, *args):
    #         return cls(self.domain)
    #     return inner
    #
    # nowplaying = proxy(NowPlaying)


class AsyncConnector:

    def __init__(self, client):
        pass

