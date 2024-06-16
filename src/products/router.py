from fastapi import APIRouter
from products.models import ProductBase
from products.service import create_product
from session_deps import SessionDep

router = APIRouter()


@router.get("/products")
def get_products(session: SessionDep, data: ProductBase):
    return create_product(session, data)
