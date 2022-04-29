from typing import TypeVar
from .base import BaseApi

Stations_T = TypeVar('Stations_T')


class Stations(BaseApi):

    __slots__ = ()

    _variations = (
        ('station',),
        ('stations',)
    )
    _content_type: str = 'JSON'

    def station(self, station_id: int) -> Stations_T:
        self._add('station', station_id)
        return self

    def stations(self) -> Stations_T:
        self._add('stations', '')
        return self



