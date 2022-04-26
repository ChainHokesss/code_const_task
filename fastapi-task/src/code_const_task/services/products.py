from ast import operator
from fastapi import Depends, HTTPException, status
from sqlalchemy import delete
from sqlalchemy.orm import Session
from ..database import get_session
from ..models.products import Product, ProductCreate, ProductUpdate
from .. import tables
from typing import List, Optional


class ProductsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, product_id: Optional[int]) -> tables.Product:
        product = self.session.query(tables.Product).filter_by(id = product_id).first()
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return product

    def get_list(self) -> List[Product]:
        products = self.session.query(tables.Product).all()
        return products

    def get(self, product_id: Optional[int] = None, product_name: Optional[str] = None) -> tables.Product:
        
        return self._get(product_id)
    
    def get_by_name(self, product_name: str) -> tables.Product:
        product = self.session.query(tables.Product).filter_by(name = product_name).first()
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return product


    def create(self, product: ProductCreate) -> tables.Product:
        product = tables.Product(**product.dict())
        self.session.add(product)
        self.session.commit()
        return product 

    def update(self, product_id: int, product_data: ProductUpdate) -> tables.Product:
        product = self._get(product_id)
        for field, value in product_data:
            setattr(product, field, value)

        self.session.commit()
        return product
    
    def delete(self, product_id: int):
        product = self._get(product_id)
        self.session.delete(product)
        self.session.commit()
