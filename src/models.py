from auth.models import User
from products.models import Product
from sqlmodel import SQLModel


class User_table(User, SQLModel):
    pass


class Products_tables(Product, SQLModel):
    pass
