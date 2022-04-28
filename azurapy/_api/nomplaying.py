from typing import TypeVar, Union
from .base import BaseApi

NowPlaying_T = TypeVar('NowPlaying_T')


class NowPlaying(BaseApi):

    __slots__ = ()

    _variations = (
        ('nowplaying',),
    )

    def nowplaying(self, station_id: Union[int, str] = '') -> NowPlaying_T:
        self._add('nowplaying', station_id)
        return self




