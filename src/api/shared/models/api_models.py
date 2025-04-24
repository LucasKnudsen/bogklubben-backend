from pydantic import BaseModel
from typing import Optional, Generic, TypeVar

T = TypeVar("T")


class APIResponse(BaseModel, Generic[T]):
    message: Optional[str] = None
    data: T
