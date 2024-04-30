from datetime import datetime, timedelta

import jwt
from core.config import settings
from passlib.context import CryptContext  # type: ignore

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verific_password_hash(password: str, hash_password) -> str:
    return pwd_context.verify(password, hash_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(subject: str, token_expire: timedelta) -> str:
    expire_data = datetime.utcnow() + token_expire
    encode = jwt.encode(
        {"id": subject, "exp": expire_data}, settings.SECRET_KEY, algorithm="HS256"
    )
    return encode
