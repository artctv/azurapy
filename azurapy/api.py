from ._api import (
    MountPoints
)


class ApiWrapper:

    @property
    def mount_points(self) -> MountPoints: return MountPoints()


api = ApiWrapper()
