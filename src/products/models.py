from decimal import Decimal
from typing import List, Optional
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class ProductBase(SQLModel):
    name: str
    description: str
    price: Decimal = Field(default=0, max_digits=5, decimal_places=3)
    img_product: Optional[str] = None


class Product(ProductBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)


class ProductCreate(ProductBase):
    ingredients: List[str]


class Ingredient(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    id_product: Optional[UUID] = Field(default=None, foreign_key="product.id")
