# tests_man/test.py

import sys
import os
import bcrypt

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Monkey-patch bcrypt to add __about__.__version__
class BcryptAbout:
    __version__ = "4.2.1"

bcrypt.__about__ = BcryptAbout()

# Import all models to ensure they are registered with Base
from app.models import role, user, student

from app.db import get_db
from tests_man.test_user import test_create_user
from app.models.user import User  # Ensure User is imported

def main():
    # Obtain the generator
    db_generator = get_db()
    
    try:
        # Get the next item from the generator, which is the db session
        db = next(db_generator)
        
        assert db, "Failed to create a database session."
        
        # Run the test
        test_create_user(db)
        
        print("Test passed successfully.")
        
    except Exception as e:
        print(f"An error occurred during testing: {e}")
    finally:
        # Close the session properly
        try:
            db.close()
            next(db_generator, None)
        except:
            pass

if __name__ == "__main__":
    main()



