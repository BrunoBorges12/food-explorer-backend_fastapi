from core.config import settings
from sqlmodel import create_engine

print(settings.SQLALCHEMY_DATABASE_URI)

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))
