from typing import Annotated

from auth.security import verific_token
from fastapi import APIRouter, Depends
from products.models import ProductBase
from session_deps import SessionDep

router = APIRouter()


@router.post("/products")
def get_products(
    session: SessionDep,
    data: ProductBase,
    token: Annotated[str, Depends(verific_token)],
):
    return token
