from pydantic import BaseModel, constr

class UserBase(BaseModel):
    image: bytes

class UserCreate(UserBase):
    name: constr(min_length=1, max_length=30)

class UserUpdate(UserBase):
    id: int

class User(UserBase):
    id: int
    name: constr(min_length=1, max_length=30)

    class Config:
        orm_mode = True
