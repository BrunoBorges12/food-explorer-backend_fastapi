from datetime import datetime, timedelta
from typing import Annotated

import jwt
from core.config import settings
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext  # type: ignore

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/api/login")


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


def verific_token(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        print(token)
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        return payload
    except:  # noqa: E722
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
