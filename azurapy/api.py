from ._api import (
    MountPoints,
    Stations,
    NowPlaying
)


class ApiWrapper:

    @property
    def nowplaying(self) -> NowPlaying: return NowPlaying()

    @property
    def stations(self) -> Stations: return Stations()

    @property
    def mount_points(self) -> MountPoints: return MountPoints()


api = ApiWrapper()
