from .models import nowplaying, mount_points
from .models.mount_points import MountPoints
from .models import *  # __import___


# class ParentWrapper:
#     def __init_subclass__(cls, **kwargs):
#         for attr, fucn in cls.__dict__.items():


class ModelsWrapper:

    nowplaying = nowplaying
    # mount_points = MountPoints()

    @property
    def mount_points(self):
        return MountPoints()


models = ModelsWrapper()
