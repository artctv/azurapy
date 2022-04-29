from typing import Optional
from dataclasses import dataclass, asdict


@dataclass
class BaseResponse:
    code: int

    def as_dict(self) -> dict:
        return asdict(self)


@dataclass
class Response200(BaseResponse):
    data: dict


@dataclass
class Response200File(BaseResponse):
    content: bytes


@dataclass
class BaseErrorResponse(BaseResponse):
    type: str
    message: str
    formatted_message: str
    extra_data: list
    success: bool


@dataclass
class Response403(BaseErrorResponse):
    pass


@dataclass
class Response404(BaseErrorResponse):
    pass


@dataclass
class Response500(BaseErrorResponse):
    pass


@dataclass
class Response302(BaseResponse):
    message: str = '302 is a redirect. You may need to add a `API_KEY'


@dataclass
class ResponseAny(BaseResponse):
    text: Optional[str] = None
