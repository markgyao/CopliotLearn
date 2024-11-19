from pydantic import BaseModel
from typing import Optional

class PermissionBase(BaseModel):
    permission_name: str
    description: Optional[str] = None
    resource: str
    action: str

class PermissionCreate(PermissionBase):
    pass

class Permission(PermissionBase):
    id: int

    class Config:
        orm_mode = True