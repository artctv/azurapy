from typing import Dict, TypeVar, Union
from ssl import SSLContext
from functools import partial
import httpx
from .client import AzuraCastClient
from ._api.base import BaseApi
from .utils import (
    Response200,
    Response200File,
    Response302,
    Response403,
    Response404,
    Response500,
    ResponseAny
)

Connector_T = TypeVar('Connector_T', bound='Connector')
BaseApi_T = TypeVar('BaseApi_T', bound=BaseApi)
Responses_T = Union[Response200, Response200File, Response302, Response403, Response404, Response500, ResponseAny]


class Connector:

    azura_client: AzuraCastClient
    as_dataclass: bool

    _api_headers: Union[Dict[str, str], Dict]
    _ssl_context: Union[SSLContext, bool]
    _client: partial

    __url: str
    __type: str

    # todo: add httpx limits and timeout
    def __init__(self, azura_client: AzuraCastClient, as_dataclass: bool = False) -> None:
        self.azura_client = azura_client
        self.as_dataclass = as_dataclass
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
            verify=verify,
        )

    def __call__(self, api: BaseApi_T) -> Connector_T:
        if not api._check():  # noqa
            raise AttributeError('Unavailable combination for `api`')
        self.__url, self.__type = api._compile()  # noqa
        return self

    @staticmethod
    def _parse_errors_response(r: httpx.Response) -> Union[Response403, Response404, Response500]:
        if r.status_code == 403:
            return Response403(**r.json())
        elif r.status_code == 404:
            return Response404(**r.json())
        else:
            return Response500(**r.json())

    @staticmethod
    def _parse_302_response(r: httpx.Response) -> Response302:
        return Response302(code=r.status_code)

    @staticmethod
    def _parse_200_response(r: httpx.Response) -> Response200:
        return Response200(code=r.status_code, data=r.json())

    def _parse_response(self, r: httpx.Response) -> Union[dict, Responses_T]:
        if r.status_code in {403, 404, 500}:
            response = self._parse_errors_response(r)
        elif r.status_code == 302:
            response = self._parse_302_response(r)
        elif r.status_code == 200:
            response = self._parse_200_response(r)
        else:
            response = ResponseAny(code=r.status_code, text=r.text)

        if not self.as_dataclass:
            return response.as_dict()
        return response

    def get(self) -> Union[dict, Responses_T]:
        client: httpx.Client
        if self.__type == 'JSON':
            with self._client() as client:
                r = client.get(self.__url)
        return self._parse_response(r)

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
