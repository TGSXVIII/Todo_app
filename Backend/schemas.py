from pydantic import BaseModel

# Schema for creating a ToDo
class ToDoCreate(BaseModel):
    title: str
    description: str

# Schema for returning a ToDo with all fields
class ToDoBase(BaseModel):
    id: int
    title: str
    description: str
    done: int

    class Config:
        orm_mode = True
