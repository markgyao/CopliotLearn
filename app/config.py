
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
# Automatically load .env from the current working directory (no need for os)
load_dotenv()

class Settings(BaseSettings):
    database_url: str
    secret_key: str

    class Config:
        env_file = ".env"  # Pydantic will also look for the .env file automatically in cwd
        extra = 'allow'  # Use a literal string instead of Extra.allow

settings = Settings()

