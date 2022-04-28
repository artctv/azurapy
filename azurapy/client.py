from typing import ClassVar, Optional, Union
from pathlib import Path


class AzuraCastClient:
    domain: str
    api_key: Optional[str]
    ssl_cert: Optional[Union[str, Path]]
    base_url: str

    _domain: str
    _api_postfix: ClassVar[str] = '/api'

    def __init__(
        self,
        domain: str,
        api_key: Optional[str] = None,
        ssl_cert: Optional[Union[str, Path]] = None
    ):
        self.domain = domain
        self.api_key = api_key
        self.ssl_cert = ssl_cert

    @property
    def domain(self) -> str: return self._domain

    @domain.setter
    def domain(self, value: str) -> None:
        if 'http://' not in value and 'https://' not in value:
            raise AttributeError('`domain` must start with `http://` or `https://`')
        self._domain = value.rstrip('/')

    @property
    def base_url(self) -> str: return f'{self.domain}{self._api_postfix}'

    def set_api_postfix(self, value: str) -> None:
        """If for some reason in your version of AzuraCast the `/api`
        subpath is changed, use this method to override it"""
        self._api_postfix = value
