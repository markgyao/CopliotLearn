from dotenv import load_dotenv
from pydantic_settings import BaseSettings
import os
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="pydantic") 
#hides the warning message from pydantic "UserWarning: Valid config keys have changed in V2: * 'orm_mode' has been renamed to 'from_attributes'  warnings.warn(message, UserWarning)"

# Load the .env file dynamically
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

class Settings(BaseSettings):
    database_url: str
    secret_key: str

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), ".env")  # Dynamically resolve .env path
        from_attributes = True  # New Pydantic v2 option replacing `warn_unused`

settings = Settings()

# Debugging output
print(f"Database URL from settings: {settings.database_url}")
print(f"Secret Key from settings: {settings.secret_key}")