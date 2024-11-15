# app/schemas/user.py

from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    account_id: str
    last_name: str
    first_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    wechat_id: Optional[str] = None
    is_active: int = 0

class UserCreate(UserBase):
    password: str  # Changed from 'password_hash' to 'password'
    role_id: int   # Include role_id during user creation

class User(UserBase):
    id: int
    role_id: int

    class Config:
        from_attributes = True
