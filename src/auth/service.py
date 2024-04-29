from auth.models import User, UserCreate
from auth.security import get_password_hash
from sqlmodel import Session, select


def create_user(session: Session, user_create: UserCreate):
    db_obj = User.model_validate(
        user_create, update={"hashed_password": get_password_hash(user_create.password)}
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def get_user_by_email(session: Session, email: str) -> str:
    is_email = select(User).where(User.email == email)
    user = session.exec(is_email).first()
    return user
