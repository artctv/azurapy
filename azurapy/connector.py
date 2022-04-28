from typing import Dict, TypeVar, Union
from ssl import SSLContext
from functools import partial
import httpx
from .client import AzuraCastClient
from ._api.base import BaseApi

Connector_T = TypeVar('Connector_T', bound='Connector')
BaseApi_T = TypeVar('BaseApi_T', bound=BaseApi)


class Connector:

    azura_client: AzuraCastClient

    _api_headers: Union[Dict[str, str], Dict]
    _ssl_context: Union[SSLContext, bool]
    _client: partial

    __state: str

    def __init__(self, azura_client: AzuraCastClient) -> None:  # todo: add httpx limits and timeout
        self.azura_client = azura_client
        self._api_headers = self.set_up_api_headers(azura_client)
        self._ssl_context = self.set_up_ssl_context(azura_client)
        self._client = self.set_up_client(self.azura_client, self._api_headers, self._ssl_context)

    @staticmethod
    def set_up_api_headers(azura_client: AzuraCastClient) -> Union[Dict[str, str], Dict]:
        if azura_client.api_key:
            return {'Authorization': f'Bearer {azura_client.api_key}'}
        return {}

    @staticmethod
    def set_up_ssl_context(azura_client: AzuraCastClient) -> Union[SSLContext, bool]:
        if azura_client.ssl_cert:
            return httpx.create_ssl_context(verify=azura_client.ssl_cert)
        return False

    @staticmethod
    def set_up_client(
        azura_client: AzuraCastClient,
        headers: dict,
        verify: Union[SSLContext, bool]
    ) -> partial:
        return partial(
            httpx.Client,
            base_url=azura_client.base_url,
            headers=headers,
            verify=verify
        )

    def __call__(self, api: BaseApi_T) -> Connector_T:
        if not api._check():  # noqa
            raise AttributeError('Unavailable combination for `api`')
        self.__state = api._compile()  # noqa
        return self

    def get(self) -> dict:
        with self._client() as client:
            client: httpx.Client
            r = client.get(self.__state)
        self.__state = ''
        return r.json()

    def post(self):
        pass

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass

    def __del__(self):
        self._client().close()
