import os
import mariadb
from mariadb import Error
from passlib.context import CryptContext
from dotenv import load_dotenv
from urllib.parse import urlparse

# Load environment variables from .env file
load_dotenv()

# Get database connection details from environment variables
db_url = os.getenv('DATABASE_URL')
secret_key = os.getenv('SECRET_KEY')

# Parse the DATABASE_URL
url = urlparse(db_url)
db_config = {
    'host': url.hostname,
    'user': url.username,
    'password': url.password,
    'database': url.path[1:],  # Remove leading '/'
    'port': url.port
}

# Initialize password context with bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], bcrypt__default_rounds=12)

# Function to update user password and activate user
def configure_user(account_id, new_password):
    try:
        # Connect to the MariaDB database
        connection = mariadb.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database'],
            port=db_config['port']
        )

        if connection:
            cursor = connection.cursor()

            # Hash the new password
            hashed_password = pwd_context.hash(new_password)

            # Update the user's password and activate the user
            update_query = """
            UPDATE users
            SET password_hash = %s, is_active = %s
            WHERE account_id = %s
            """
            cursor.execute(update_query, (hashed_password, True, account_id))

            # Commit the changes
            connection.commit()

            print(f"User '{account_id}' has been updated successfully.")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

# Example usage
if __name__ == "__main__":
    account_id = input("Enter the account ID: ")
    new_password = input("Enter the new password: ")
    configure_user(account_id, new_password)