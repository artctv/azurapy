import httpx
from .wrapper import ModelsWrapper
from .client import AzuraCastClient


class Connector:

    wrapper: ModelsWrapper
    azura: AzuraCastClient

    def __init__(self, azura: AzuraCastClient):
        self.azura = azura
        self.wrapper = ModelsWrapper()
        self.client = httpx.Client(headers={'Authorization': f'Bearer {azura.key}'})

    # def request(self):

    def __getattr__(self, item):
        try:
            attr = getattr(self.wrapper, item)
        except AttributeError as e:
            raise AttributeError(f"Connector object has not attribute '{item}'") from e
        else:
            return attr

    # def __getattribute__(self, item):
    #     print(item, 'kek')
    #     return super().__getattribute__(item)

    def __call__(self, data, *args, **kwargs):
        url, method = data[0], data[1]
        # print(f'{self.azura.domain}{url}')
        r = self.client.request(method=method, url=f'{self.azura.domain}{url}')
        print(r.json())
        # self.client.get(url)
