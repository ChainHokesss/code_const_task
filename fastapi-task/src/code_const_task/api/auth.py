from urllib import response
from fastapi import Depends, Form, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi.routing import APIRouter
from typing import Optional
from ..models.auth import User, Role, UserCreate, Token
from .. import tables

from ..services.auth import AuthService, get_current_user
from fastapi.responses import RedirectResponse


router = APIRouter(
    prefix="/auth"
)



@router.get("/all_users")
def get_all_users(service: AuthService = Depends(), role: Optional[Role] = None):
    users = service.get_list(role = role)
    return users


@router.post(
    '/sign-up/',
    response_model=Token,
    status_code=status.HTTP_201_CREATED,
)
def sign_up(
    user_data: UserCreate,
    auth_service: AuthService = Depends(),
):
    return auth_service.register_new_user(user_data)


@router.post(
    '/sign-in/',
    response_model=Token,
)
def sign_in(
    auth_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(),
):
    return auth_service.authenticate_user(
        auth_data.username,
        auth_data.password,
    )
    
@router.get('/my_user', response_model=User)
def get_my_user(user: User = Depends(get_current_user)):
    return user