from .client import AzuraCastClient
from .connector import Connector
from .api import api


__title__ = "azurapy"
__description__ = """
    Unofficial python API integration for AzuraCast:
    free and open-source self hosted web radio management suite
"""
__version__ = "0.0.1"

__all__ = [
    "__description__",
    "__title__",
    "__version__",
    "AzuraCastClient",
    "Connector",
    "api"
]
