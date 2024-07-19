from datetime import timedelta
from typing import Annotated

from auth.models import Token, UserCreate
from auth.security import create_access_token
from auth.service import authentication, create_user, get_user_by_email
from core.config import settings
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from session_deps import SessionDep

router = APIRouter()


@router.post("/register")
async def create_users(session: SessionDep, user: UserCreate):
    user_db = get_user_by_email(session, user.email)
    if user_db:
        raise HTTPException(
            status_code=400,
            detail="O usuário com este e-mail já existe no sistema",
        )
    return create_user(session, user)


@router.post(
    "/login",
)
async def login(
    session: SessionDep, user: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user_login = authentication(session, email=user.username, password=user.password)
    if not user_login:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Email ou senha incorreto"
        )
    if not user_login.is_active:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Usuario Inativo")
    acess_token_expirer = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return Token(
        access_token=create_access_token(
            user_login.id,
            acess_token_expirer,
            user_login.is_superuser,
            user_login.is_active,
        )
    )
