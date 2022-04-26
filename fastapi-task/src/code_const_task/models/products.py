from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    number: int 

    class Config:
        orm_mode = True


class Product(ProductBase):
    id: int
    price: int


class ProductCreate(ProductBase):
    price: int

class ProductUpdate(ProductBase):
    price: int

class ProductBuy(ProductBase):
    pass