from typing import TypeVar
from .base import BaseApi

MountPoints_T = TypeVar('MountPoints_T')


class MountPoints(BaseApi):

    __slots__ = ()

    _variations = (
        ('station', 'mount', 'intro'),
        ('station', 'mounts'),
        ('station', 'mount')
    )

    def station(self, station_id: int) -> MountPoints_T:
        self._add('station', station_id)
        return self

    def mount(self, mount_id: int) -> MountPoints_T:
        self._add('mount', mount_id)
        return self

    def mounts(self) -> MountPoints_T:
        self._add('mounts', '')
        return self

    def intro(self) -> MountPoints_T:
        self._add('intro', '')
        return self

