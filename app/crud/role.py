from sqlalchemy.orm import Session
from app.models.role import Role
from app.schemas.role import RoleCreate

def create_role(db: Session, role: RoleCreate):
    db_role = Role(role_name=role.role_name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

# Function to fetch all roles
def get_all_roles(db: Session):
    return db.query(Role).all()

def get_role(db: Session, role_id: int):
    return db.query(Role).filter(Role.id == role_id).first()

def get_roles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Role).offset(skip).limit(limit).all()

def delete_role(db: Session, role_id: int):
    db_role = get_role(db, role_id)
    if db_role:
        db.delete(db_role)
        db.commit()
    return db_role
