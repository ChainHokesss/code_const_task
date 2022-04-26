from pydantic import BaseModel
from typing import Optional 
from enum import Enum


class Role(str, Enum):
    seller = 'seller'
    buyer = 'buyer'

class UserBase(BaseModel):
    username: str
    role: Optional[Role] = None

    class Config:
        orm_mode = True


class User(UserBase):
    id:int 


class UserCreate(UserBase):
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'