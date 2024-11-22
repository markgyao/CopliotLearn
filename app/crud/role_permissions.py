from sqlalchemy.orm import Session
from app.models.role_permission import RolePermission

# Create a new role permission record in the database
def create_role_permission(db: Session, role_id: int, permission_id: int):
    db_role_permission = RolePermission(role_id=role_id, permission_id=permission_id)
    db.add(db_role_permission)
    db.commit()
    db.refresh(db_role_permission)
    return db_role_permission

# Retrieve a role permission record by role ID and permission ID
def get_role_permission(db: Session, role_id: int, permission_id: int):
    return db.query(RolePermission).filter(RolePermission.role_id == role_id, RolePermission.permission_id == permission_id).first()

# Retrieve all role permission records
def get_all_role_permissions(db: Session):
    return db.query(RolePermission).all()

# Retrieve a limited number of role permission records with optional offset
def get_role_permissions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(RolePermission).offset(skip).limit(skip).all()

# Delete a role permission record by role ID and permission ID
def delete_role_permission(db: Session, role_id: int, permission_id: int):
    db_role_permission = get_role_permission(db, role_id, permission_id)
    if db_role_permission:
        db.delete(db_role_permission)
        db.commit()
    return db_role_permission