from decimal import Decimal
from typing import Optional

from sqlmodel import Field, SQLModel


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    price: Decimal = Field(default=0, max_digits=5, decimal_places=3)
