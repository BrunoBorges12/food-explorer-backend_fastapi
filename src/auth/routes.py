from auth.models import UserCreate
from auth.service import create_user, get_user_by_email
from fastapi import APIRouter, HTTPException
from session_deps import SessionDep

router = APIRouter()


@router.get("/register/")
async def read_users(session: SessionDep, user: UserCreate):
    is_email = get_user_by_email(session, user.email)
    print(is_email)
    if is_email:
        return HTTPException(status_code=400, detail="O usuário com este e-mail já existe no sistema")
    return create_user(session, user)
