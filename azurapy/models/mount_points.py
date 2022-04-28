from typing import TypeVar
from .base import BaseModel

MountPoints_T = TypeVar('MountPoints_T')


class MountPoints(BaseModel):

    def station(self, station_id: int) -> MountPoints_T:
        self.url = f'{self.url}/station/{station_id}'
        return self

    def mount(self, mount_id: int) -> MountPoints_T:
        self.url = f'{self.url}/mount/{mount_id}'
        return self

    def mounts(self) -> MountPoints_T:
        self.url = f'{self.url}/mounts'
        return self

    def intro(self) -> MountPoints_T:
        self.url = f'{self.url}/intro'
        return self
