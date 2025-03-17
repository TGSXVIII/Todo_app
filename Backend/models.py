from sqlalchemy import Column, Integer, String
from .database import Base

# Define the ToDo model
class ToDo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    done = Column(Integer, default=0)  # 0: not done, 1: done
