from sqlalchemy import Column, Integer, String, text, TIMESTAMP
from pydantic import BaseModel, UUID1
from sqlalchemy.orm import mapped_column, declarative_base, Mapped
from sqlalchemy import Uuid

Base = declarative_base()

class Token(Base):
    __tablename__ = 'tokens'
    client_id: Mapped[int] = mapped_column(primary_key=True)
    access_scope: Mapped[str] = mapped_column(String)
    access_token: Mapped[str] = mapped_column(
        String(22),
    server_default=text("SUBSTR(UPPER(md5(random()::text)), 2, 22)"))
    expiration_time: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP,
    server_default=text("current_timestamp + interval '2 hours'"))
    token_type: Mapped[str] = mapped_column(
        String(22),
    server_default="'Bearer'")

class User(Base):
    __tablename__ = 'users'
    client_id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    username: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
    client_secret: Mapped[str] = mapped_column(String(100))
    scope: Mapped[str] = mapped_column(String)



