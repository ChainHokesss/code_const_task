from fastapi.routing import APIRouter
from .auth import router as auth_router
from .products_operations import router as products_router


router = APIRouter()
router.include_router(auth_router)
router.include_router(products_router)
