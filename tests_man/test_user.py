# app/tests/test_user_creation.py
import uuid
from sqlalchemy.orm import Session
from app.crud.user import create_user, delete_user
from app.schemas.user import UserCreate
from app.models.user import User
from app.models.role import Role

def test_create_user(db: Session):
    # Generate a unique identifier
    unique_id = uuid.uuid4().hex[:8]
    account_id = f"tuser_{unique_id}"
    email = f"{account_id}@gmail.com"
    
    # Ensure role_id=3 exists
    role = db.query(Role).filter_by(id=3).first()
    assert role is not None, "Role with id=3 does not exist."
    
    user_data = UserCreate(
        account_id=account_id,
        last_name="tuser",
        first_name="student1",
        email=email,
        phone="212-555-1212",
        wechat_id="string",
        password="securepassword123",
        role_id=3
    )
    user = create_user(db, user_data)
    
    # Fetch the user from the database to ensure it was created correctly
    fetched_user = db.query(User).filter_by(account_id=account_id).first()
    
    assert user.id is not None, "User ID should be assigned by the database."
    assert user.created_at is not None, "created_at should be set by the database."
    assert user.updated_at is not None, "updated_at should be set by the database."
    assert user.account_id == account_id, "Account ID does not match."
    assert user.email == email, "Email does not match."
    assert user.role_id == 3, "Role ID does not match."
    assert fetched_user is not None, "User was not fetched correctly from the database."
    
    # Clean up by deleting the test user
    delete_user(db, user.id)
