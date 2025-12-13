from fastapi import APIRouter, Depends, Response, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .schemas import Token as TokenSchema, UserCreate
from .auth import (
    authenticate_user,
    create_user as create_user_auth,
    create_access_token,
    oauth2_scheme,
)
from database import get_db

router = APIRouter()


@router.post("/register", response_model=UserCreate)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    create_user_auth(db, user)
    return user


@router.post("/token", response_model=TokenSchema)
def login_for_access_token(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = create_access_token({"sub": user.username})
    return {
        "client_id": user.client_id,
        "access_token": access_token,
        "access_scope": getattr(user, "scope", ""),
        "token_type": "Bearer",
        "expires_in": 60 * 60 * 2,
    }


@router.get("/check")
def check_user(token: str = Depends(oauth2_scheme)):
    return {"Authorization": f"Bearer {token}"}

