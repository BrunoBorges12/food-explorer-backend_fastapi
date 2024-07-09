from auth.security import verific_token
from fastapi import APIRouter, Depends, HTTPException
from products.models import ProductBase
from products.service import list_product
from session_deps import SessionDep

router = APIRouter(dependencies=[Depends(verific_token)])


@router.post(
    "/create_product",
)
def create_product(
    session: SessionDep,
    data: ProductBase,
):
    return "foi"


@router.post(
    "/product/{id}",
)
def product(session: SessionDep, id: int):
    product = list_product(session, id)
    if not product:
        raise HTTPException(status_code=404, detail="Não existe esse produto")
    return product
