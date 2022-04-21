from typing import Union, Optional
from pathlib import Path
from .wrapper import ModelsWrapper


class AzuraCastClient:
    domain: str
    key: str
    ssl_key: Optional[Union[str, Path]]

    def __init__(self, domain: str, key: str, ssl_key: Optional[Union[str, Path]] = None):
        self.domain = domain
        self.key = key
        self.ssl_key = ssl_key
        self.wrapper = ModelsWrapper()

    def __getattr__(self, item):
        try:
            attr = getattr(self.wrapper, item)
        except AttributeError as e:
            raise AttributeError(f"Connector object has not attribute '{item}'") from e
        else:
            return attr

