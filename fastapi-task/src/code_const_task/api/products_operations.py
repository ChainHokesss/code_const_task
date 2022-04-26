from importlib.metadata import packages_distributions
from itertools import product
from typing import List
from webbrowser import get
from fastapi import APIRouter, Depends, HTTPException, status
from ..models.products import Product, ProductBuy, ProductCreate, ProductUpdate
from .. import tables
from sqlalchemy.orm import Session
from ..database import get_session
from ..services.products import ProductsService
from ..services.auth import get_current_user
from ..models.auth import User


router = APIRouter(
    prefix='/products'
)


@router.get("/all", response_model=List[Product])
def get_all_products(service: ProductsService = Depends()):

    products = service.get_list()

    return products


@router.get("/{product_id}", response_model=Product)
def get_product(product_id, service: ProductsService = Depends()):
    return service.get(product_id)


@router.post("/create_product", response_model=Product)
def create_product(product: ProductCreate, service: ProductsService = Depends(), user: User = Depends(get_current_user)):
    if not user.role == 'seller':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return service.create(product)


@router.put("/update/{product_id}", response_model=Product)
def update_product(product_id: int, product: ProductUpdate, service: ProductsService = Depends(), user: User = Depends(get_current_user)):
    if not user.role == 'seller':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return service.update(product_id, product)


@router.post("/buy-product", response_model=Product)
def buy_product(product_data: ProductBuy, service: ProductsService = Depends(), user: User = Depends(get_current_user)):
    if not user.role == 'buyer':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    
    product = service.get_by_name(product_data.name)

    if product.number < product_data.number:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    product_update: ProductUpdate = ProductUpdate(**product_data.dict(), price = product.price)

    product_data.number = product.number - product_data.number

    for field, value in product_data:
        setattr(product_update, field, value)


    return service.update(product.id, product_update)
