from sqlalchemy.orm import Session
from app.models.permissions import Permission
from app.schemas.permissions import PermissionCreate

# Create a new permission in the database
def create_permission(db: Session, permission: PermissionCreate):
    db_permission = Permission(**permission.dict())
    db.add(db_permission)
    db.commit()
    db.refresh(db_permission)
    return db_permission

# Fetch a permission by its ID
def get_permission(db: Session, permission_id: int):
    return db.query(Permission).filter(Permission.id == permission_id).first()

# Fetch a permission by its name
def get_permission_by_name(db: Session, permission_name: str):
    return db.query(Permission).filter(Permission.permission_name == permission_name).first()

# Fetch all permissions from the database
def get_all_permissions(db: Session):
    return db.query(Permission).all()

# Fetch a limited number of permissions with optional offset
def get_permissions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Permission).offset(skip).limit(limit).all()

# Delete a permission by its ID
def delete_permission(db: Session, permission_id: int):
    db_permission = get_permission(db, permission_id)
    if db_permission:
        db.delete(db_permission)
        db.commit()
    return db_permission