from decimal import Decimal
from uuid import UUID

from auth.security import verific_token
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from products.models import ProductBase
from products.service import create_product as create_product_service
from products.service import list_product
from session_deps import SessionDep
from utils.create_file import create_file

router = APIRouter(dependencies=[Depends(verific_token)])


@router.post("/create_product", response_model=ProductBase)
def create_product(
    session: SessionDep,
    name: str = Form(),
    description: str = Form(),
    file: UploadFile = File(),
    price: Decimal = Form(default=0),
):
    upload_file_name = create_file(file)

    if upload_file_name["filename"] is not None:
        product_dict_model = ProductBase(
            name=name,
            description=description,
            img_product=upload_file_name["filename"],
            price=price,
        )
        product = create_product_service(session, product_dict_model)
        return product
    else:
        raise HTTPException(status_code=404, detail=upload_file_name["message"])


@router.post(
    "/product/{id}",
)
def product(session: SessionDep, id: UUID):
    product = list_product(session, id)
    if not product:
        raise HTTPException(status_code=404, detail="Não existe esse produto")
    return product
