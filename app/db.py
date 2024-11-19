from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
import logging

# Configure logging for the database operations
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database URL from your .env file or configuration
DATABASE_URL = settings.database_url

# Step 1: Create a SQLAlchemy engine with connection pooling
# Customize pool settings: pool_size, max_overflow, pool_recycle, pool_timeout
engine = create_engine(
    DATABASE_URL,
    pool_size=10,            # Max number of connections in the pool
    max_overflow=20,         # Max additional connections above pool_size
    pool_recycle=3600,       # Recycle connections after 1 hour (3600 seconds)
    pool_timeout=30          # Timeout to get a connection from the pool (30 seconds)
)

# Step 2: Create a session factory (SessionLocal) bound to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Step 3: Create a declarative base class for models
Base = declarative_base()

# Step 4: Dependency for getting a database session for each request
def get_db():
    """
    Dependency that provides a SQLAlchemy session for the duration of a request.
    It yields a session and ensures the session is closed after the request, returning
    the connection back to the connection pool.
    """
    db = SessionLocal()  # Create a new session
    try:
        yield db  # Yield the session for use in the API call
    except SQLAlchemyError as e:
        # Handle any database-related exceptions
        logger.error(f"Database error: {str(e)}")
        db.rollback()  # Rollback any changes if an error occurs
        raise
    finally:
        # Always close the session after use, returning the connection to the pool
        db.close()
        logger.info("Database session closed and connection returned to the pool")
