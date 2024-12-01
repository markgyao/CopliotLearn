from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import hash_password

def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)
    db_user = User(**user.dict(exclude={'password'}))
    db_user.password_hash = hashed_password
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
# ... (rest of the file remains the same)
def get_user_by_account_id(db: Session, account_id: str):
    return db.query(User).filter(User.account_id == account_id).first()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_all_users(db: Session):
    return db.query(User).all()  # This will return all users in the 'users' table

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
