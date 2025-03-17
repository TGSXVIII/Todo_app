from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL (replace with your database URL)
SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost:5432/todo_app"

# Create a database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a sessionmaker to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
