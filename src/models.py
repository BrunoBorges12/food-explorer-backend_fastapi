from sqlmodel import SQLModel

from src.auth.models import User
from src.products.models import Ingredient, Product


class UserTable(User, SQLModel):
    pass


class ProductsTables(Product, SQLModel):
    pass


class IngredientTable(Ingredient, SQLModel):
    pass
