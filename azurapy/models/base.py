

class BaseModel:

    _url: str

    def __init__(self):
        self.url = str()

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, value: str) -> None:
        self._url = value

    def clear(self) -> None:
        self.url = str()
