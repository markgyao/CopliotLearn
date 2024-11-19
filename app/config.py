import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load .env file manually (explicitly)
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

class Settings(BaseSettings):
    database_url: str
    secret_key: str

    class Config:
        env_file = ".env"  # Pydantic will also look for the .env file automatically in cwd
        extra = 'allow'  # Use a literal string instead of Extra.allow

settings = Settings()

# Debugging: Print the loaded settings
print(f"Database URL: {settings.database_url}")
print(f"Secret Key: {settings.secret_key}")