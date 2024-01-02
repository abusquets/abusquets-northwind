from fastapi.routing import APIRouter

from .category import router as category_router
from .product import router as product_router
from .supplier import router as supplier_router


router = APIRouter(prefix='/northwind', tags=['northwind'])
router.include_router(category_router)
router.include_router(supplier_router)
router.include_router(product_router)
