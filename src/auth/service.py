from auth.models import User, UserCreate
from auth.security import get_password_hash, verific_password_hash
from sqlmodel import Session, select


def create_user(session: Session, user_create: UserCreate):
    db_obj = User.model_validate(
        user_create, update={"hashed_password": get_password_hash(user_create.password)}
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def get_user_by_email(session: Session, email: str) -> User:
    is_email = select(User).where(User.email == email)
    user = session.exec(is_email).first()
    return user


def authentication(session: Session, password: str, email: str):
    user_db = get_user_by_email(session=session, email=email)

    if not user_db:
        return None
    if not verific_password_hash(password, user_db.hashed_password):
        return None
    return user_db
