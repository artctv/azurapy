from .client import AzuraCastClient
from .connector import Connector


__title__ = "azurapy"
__description__ = """
    Simple python API integration for AzuraCast:
    free and open-source self hosted web radio management suite
"""
__version__ = "0.0.2"

__all__ = [
    "AzuraCastClient",
    "Connector",
    "__description__",
    "__title__",
    "__version__",
]
