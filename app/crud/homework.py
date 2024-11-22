# from sqlalchemy.orm import Session
# from app.models.homework import Homework
# from app.schemas.homework import HomeworkCreate

# # Create a new homework record in the database
# def create_homework(db: Session, homework: HomeworkCreate):
#     db_homework = Homework(**homework.dict())
#     db.add(db_homework)
#     db.commit()
#     db.refresh(db_homework)
#     return db_homework

# # Retrieve a homework record by its ID
# def get_homework(db: Session, homework_id: int):
#     return db.query(Homework).filter(Homework.id == homework_id).first()

# # Retrieve all homework records
# def get_all_homeworks(db: Session):
#     return db.query(Homework).all()

# # Retrieve a limited number of homework records with optional offset
# def get_homeworks(db: Session, skip: int = 0, limit: int = 10):
#     return db.query(Homework).offset(skip).limit(limit).all()

# # Delete a homework record by its ID
# def delete_homework(db: Session, homework_id: int):
#     db_homework = get_homework(db, homework_id)
#     if db_homework:
#         db.delete(db_homework)
#         db.commit()
#     return db_homework