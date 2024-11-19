from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import role_permission as crud_role_permission
from app.schemas import role_permission as schema_role_permission
from app.db import get_db

router = APIRouter()

@router.post("/role_permissions/", response_model=schema_role_permission.RolePermission)
def create_role_permission(role_permission: schema_role_permission.RolePermissionCreate, db: Session = Depends(get_db)):
    return crud_role_permission.create_role_permission(db, role_permission)

@router.get("/role_permissions", response_model=list[schema_role_permission.RolePermission])
def get_all_role_permissions(db: Session = Depends(get_db)):
    return crud_role_permission.get_all_role_permissions(db)

@router.get("/role_permissions/{role_id}/{permission_id}", response_model=schema_role_permission.RolePermission)
def get_role_permission(role_id: int, permission_id: int, db: Session = Depends(get_db)):
    db_role_permission = crud_role_permission.get_role_permission(db, role_id, permission_id)
    if db_role_permission is None:
        raise HTTPException(status_code=404, detail="RolePermission not found")
    return db_role_permission

@router.delete("/role_permissions/{role_id}/{permission_id}")
def delete_role_permission(role_id: int, permission_id: int, db: Session = Depends(get_db)):
    return crud_role_permission.delete_role_permission(db, role_id, permission_id)