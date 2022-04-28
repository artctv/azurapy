from typing import Union, Optional
from pathlib import Path
import httpx
from .wrapper import ModelsWrapper


class AzuraCastClient:
    domain: str
    key: str
    ssl_key: Optional[Union[str, Path]]

    def __init__(self, domain: str, key: str, ssl_key: Optional[Union[str, Path]] = None):
        self.domain = self._parse_domain(domain)
        self.base_url = self.domain+'/api'
        self.key = key
        self.ssl_key = ssl_key
        self.client = httpx.Client(headers={'Authorization': f'Bearer {key}'})
            
    @staticmethod        
    def _parse_domain(domain: str) -> str:
        return domain.rstrip('/')

    def _parse_url(self, url: str) -> str:
        return f'''{self.base_url}/{url.lstrip('/')}'''

    def __call__(self, request, *args, **kwargs):
        url, method = self._parse_url(request.url), request.method
        r = self.client.request(method=method, url=url)
        return r.json()
        # parse_request()   todo
        # return r.json()
        # print(r.json())
        # self.client.get(url)
        # if method == 'POST':
        #     if attr is

