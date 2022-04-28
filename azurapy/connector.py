from typing import Dict, TypeVar, Union
from ssl import SSLContext
import httpx
from .client import AzuraCastClient

Connector_T = TypeVar('Connector_T', bound='Connector')


class Connector:

    azura_client: AzuraCastClient

    _api_headers: Union[Dict[str, str], Dict]
    _ssl_context: Union[SSLContext, bool]
    _client: httpx.Client

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
    def set_up_client(azura_client: AzuraCastClient, headers: dict, verify: Union[SSLContext, bool]) -> httpx.Client:
        return httpx.Client(
            base_url=azura_client.base_url,
            headers=headers,
            verify=verify
        )

    def __call__(self) -> Connector_T:
        #  raise AttributeError('Unavailable combination for `url`')
        return self

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass

    def __del__(self):
        self._client.close()
