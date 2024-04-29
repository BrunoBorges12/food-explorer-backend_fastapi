from sqlmodel import Field, SQLModel


# Shared properties
# TODO replace email str with EmailStr when sqlmodel supports it
class UserBase(SQLModel):
    is_active: bool = True
    is_superuser: bool = False
    full_name: str | None = None


# Database model, database table inferred from class name
class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str
