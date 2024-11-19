from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    account_id: str
    last_name: str
    first_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    wechat_id: Optional[str] = None
    is_active: bool = False

class UserCreate(UserBase):
    password: str
    role_id: int

class User(UserBase):
    id: int
    role_id: int

    class Config:
        orm_mode = True