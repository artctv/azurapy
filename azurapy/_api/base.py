from typing import Dict, Tuple, TypeVar, Union
from abc import ABC, abstractmethod, ABCMeta

BaseModel_T = TypeVar('BaseModel_T', bound='BaseModel')


class AbstractApi(ABC):

    __slots__ = ()

    @abstractmethod
    def _variations(self) -> Tuple[Tuple[str]]: pass



class BaseApi(AbstractApi):  # noqa

    __slots__ = ('_cache',)

    _cache: Dict[str, Union[str, int]]

    def __init__(self) -> None:
        self._cache = {}

    def _add(self, key: str, value: Union[str, int]) -> None:
        self._cache[key] = value

    def _check(self) -> bool:
        if tuple(self._cache.keys()) in self._variations:
            return True
        return False

    def _compile(self) -> str:
        url = ''
        for key, value in self._cache.items():
            url = f'{url}/{key}'
            if value:
                url = f'{url}/{value}'
        return url
