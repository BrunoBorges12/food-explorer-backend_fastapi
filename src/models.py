from sqlmodel import SQLModel

from src.auth.models import User

# Shared properties
# TODO replace email str with EmailStr when sqlmodel supports it


# Database model, database table inferred from class name
class User_table(User, SQLModel):
    pass
