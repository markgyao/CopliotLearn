# from sqlalchemy.orm import Session
# from app.models.class_models import Class
# from app.schemas.class_schemas import ClassCreate

# # Create a new class record in the database
# def create_class(db: Session, class_: ClassCreate):
#     db_class = Class(**class_.dict())
#     db.add(db_class)
#     db.commit()
#     db.refresh(db_class)
#     return db_class

# # Retrieve a class record by its ID
# def get_class(db: Session, class_id: int):
#     return db.query(Class).filter(Class.id == class_id).first()

# # Retrieve all class records
# def get_all_classes(db: Session):
#     return db.query(Class).all()

# # Retrieve a limited number of class records with optional offset
# def get_classes(db: Session, skip: int = 0, limit: int = 10):
#     return db.query(Class).offset(skip).limit(limit).all()

# # Delete a class record by its ID
# def delete_class(db: Session, class_id: int):
#     db_class = get_class(db, class_id)
#     if db_class:
#         db.delete(db_class)
#         db.commit()
#     return db_class