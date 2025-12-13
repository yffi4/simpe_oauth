from pydantic import BaseModel


class User(BaseModel):
    client_id: int
    username: str
    password: str
    client_secret: str
    scope: str

    class Config:
        from_attributes = True


class Token(BaseModel):
    client_id: int
    access_token: str
    access_scope: str
    token_type: str
    expires_in: int


class UserCreate(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str

