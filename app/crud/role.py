# from sqlalchemy.orm import Session
# from app.models.role import Role
# from app.schemas.role import RoleCreate

# # Create a new role in the database
# def create_role(db: Session, role: RoleCreate):
#     db_role = Role(role_name=role.role_name)
#     db.add(db_role)
#     db.commit()
#     db.refresh(db_role)
#     return db_role

# # Fetch all roles from the database
# def get_all_roles(db: Session):
#     return db.query(Role).all()

# # Fetch a role by its ID
# def get_role(db: Session, role_id: int):
#     return db.query(Role).filter(Role.id == role_id).first()

# # Fetch a limited number of roles with optional offset
# def get_roles(db: Session, skip: int = 0, limit: int = 10):
#     return db.query(Role).offset(skip).limit(limit).all()

# # Delete a role by its ID
# def delete_role(db: Session, role_id: int):
#     db_role = get_role(db, role_id)
#     if db_role:
#         db.delete(db_role)
#         db.commit()
#     return db_role
