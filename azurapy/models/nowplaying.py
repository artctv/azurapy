from dataclasses import dataclass
# from typing import Literal


# METHOD_T = Literal['GET', 'POST', 'PUT', 'PATCH', 'DELETE']


@dataclass
class Request:
    method: str
    url: str


def _kwargs(method: str, url: str) -> Request:
    return Request(method=method, url=url)


def get() -> Request:
    return _kwargs('GET', '/nowplaying')


def get_by_station(station_id: int) -> Request:
    return _kwargs('GET', f'/nowplaying/{station_id}')



