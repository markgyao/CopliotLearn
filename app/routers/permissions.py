# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.crud import permissions as crud_permission
# from app.schemas import permissions as schema_permission
# from app.db import get_db

# router = APIRouter()

# # Create a new permission
# @router.post("/permissions/", response_model=schema_permission.Permission)
# def create_permission(permission: schema_permission.PermissionCreate, db: Session = Depends(get_db)):
#     return crud_permission.create_permission(db, permission)

# # Get all permissions
# @router.get("/permissions", response_model=list[schema_permission.Permission])
# def get_all_permissions(db: Session = Depends(get_db)):
#     return crud_permission.get_all_permissions(db)

# # Get a specific permission by permission_id
# @router.get("/permissions/{permission_id}", response_model=schema_permission.Permission)
# def get_permission(permission_id: int, db: Session = Depends(get_db)):
#     db_permission = crud_permission.get_permission(db, permission_id)
#     if db_permission is None:
#         raise HTTPException(status_code=404, detail="Permission not found")
#     return db_permission

# # Delete a specific permission by permission_id
# @router.delete("/permissions/{permission_id}")
# def delete_permission(permission_id: int, db: Session = Depends(get_db)):
#     return crud_permission.delete_permission(db, permission_id)