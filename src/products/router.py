from auth.security import verific_token
from fastapi import APIRouter, Depends
from products.models import ProductBase
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


@router.get(
    "/product/{id}",
)
def product(session: SessionDep, id: str):
    print(id)
    return id
