

class NowPlaying:
    get: str = '/nowplaying'
    get_station: str = '/nowplaying/{station_id}'
    domain: str

    def __init__(self, domain: str):
        self.domain = domain

    # def get(self, client: httpx.Client):
    #     r = self.client.get(self.url)
    #     # schemas = []
    #     # for i in r.json():
    #     #     schema = ApiNowPlaying.parse_obj(i)
    #     #     print(schema)
    #     # print(r.json())
    #
    # def get_by_station_id(self, id_: int):
    #     r = self.client.get(f'{self.url}/{id_}')
    #     print(r.json())














# import httpx
# from typing import ClassVar, Dict
# from ..const import URL, AUTHORIZATION, BEARER
# # from .schemas.models import ApiNowPlaying
#
#
# class NowPlaying:
#     endpoint: ClassVar[str] = '/nowplaying'
#     url: str
#     client: httpx.Client
#
#     def __init__(self, base_url: str) -> None:
#         self.url = URL.format(base_url=base_url, endpoint=self.endpoint)

    # def get(self, client: httpx.Client):
    #     r = self.client.get(self.url)
    #     # schemas = []
    #     # for i in r.json():
    #     #     schema = ApiNowPlaying.parse_obj(i)
    #     #     print(schema)
    #     # print(r.json())
    #
    # def get_by_station_id(self, id_: int):
    #     r = self.client.get(f'{self.url}/{id_}')
    #     print(r.json())


# import httpx
#
#
# def get(self, client: httpx.Client):
#     r = client.get()