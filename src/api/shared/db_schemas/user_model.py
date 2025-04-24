from pydantic import BaseModel


class UserModel(BaseModel):
    id: str
    name: str
    thumbnail_url: str
