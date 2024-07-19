from decimal import Decimal
from typing import Annotated
from uuid import UUID

from auth.security import verific_token
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from products.models import ProductCreate
from products.service import create_product as create_product_service
from products.service import list_product
from session_deps import SessionDep
from utils.create_file import create_file

router = APIRouter(dependencies=[Depends(verific_token)])


@router.post("/create_product", response_model=ProductCreate)
def create_product(
    user: Annotated[str, Depends(verific_token)],
    session: SessionDep,
    name: str = Form(),
    description: str = Form(),
    file: UploadFile = File(),
    price: Decimal = Form(default=0),
    ingredients: list[str] = Form(),
):
    if user["subjectAdmin"]:
        upload_file_name = create_file(file)
        if upload_file_name["filename"] is not None:
            product_dict_model = ProductCreate(
                name=name,
                description=description,
                img_product=upload_file_name["filename"],
                price=price,
                ingredients=ingredients,
            )
            product = create_product_service(session, product_dict_model)
            return ProductCreate.model_validate(
                product, update={"ingredients": ingredients}
            )
        else:
            raise HTTPException(status_code=404, detail=upload_file_name["message"])
    else:
        raise HTTPException(
            status_code=401, detail="Você não tem autorização para criar um produto"
        )


@router.post(
    "/product/{id}",
)
def product(session: SessionDep, id: UUID):
    product = list_product(session, id)
    if not product:
        raise HTTPException(status_code=404, detail="Não existe esse produto")
    return product
