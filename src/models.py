from sqlmodel import SQLModel

from src.auth.models import User
from src.products.models import Product


class User_table(User, SQLModel):
    pass


class Products_tables(Product, SQLModel):
    pass
