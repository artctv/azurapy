from typing import Dict
import httpx
# from .const import BASE_URL, AUTHORIZATION, BEARER
# from .nowplaying import NowPlaying

from typing import Union, Optional
from pathlib import Path
from .connector import Connector


class AzuraCastClient:
    domain: str
    key: str
    ssl_key: Optional[Union[str, Path]]

    def __init__(self, domain: str, key: str, ssl_key: Optional[Union[str, Path]] = None):
        self.domain = domain
        self.key = key
        self.ssl_key = ssl_key

    @property
    def connector(self):
        return Connector(self)


        # self.base_url = BASE_URL.format(domain=domain)
        # self.client = httpx.Client(
        #     headers={AUTHORIZATION: BEARER.format(API_KEY=key)}
        # )

    # def prepare(self):  # TODO: method for check api status and may be check api key is valid
    #     pass

    # @property
    # def nowplaying(self) -> NowPlaying:
    #     return NowPlaying(base_url=self.base_url, client=self.client)

