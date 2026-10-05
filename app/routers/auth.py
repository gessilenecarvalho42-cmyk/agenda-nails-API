import bcrypt

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, LoginRequest


router = APIRouter(
    prefix="/api/auth",
    tags=["Auth"]
)


def hash_password(password: str) -> str:
    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(
        User.phone == user.phone
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Telefone já cadastrado."
        )

    new_user = User(
        phone=user.phone,
        password_hash=hash_password(user.password),
        role=user.role,
        client_id=user.client_id
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post(
    "/login",
    response_model=UserResponse
)
def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.phone == login_data.phone
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Telefone ou senha inválidos."
        )

    if not verify_password(
        login_data.password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Telefone ou senha inválidos."
        )

    return user