from pydantic import BaseModel

class UserBase(BaseModel):
    image: bytes

class UserCreate(UserBase):
    name: str

class UserUpdate(UserBase):
    id: int

class User(UserBase):
    id: int
    name: str

    class Config:
        orm_mode = True
