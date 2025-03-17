from sqlalchemy.orm import Session
from . import models

# Create a new ToDo
def create_todo(db: Session, title: str, description: str):
    db_todo = models.ToDo(title=title, description=description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

# Get all ToDos
def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ToDo).offset(skip).limit(limit).all()

# Get a ToDo by ID
def get_todo_by_id(db: Session, todo_id: int):
    return db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()

# Update a ToDo by ID
def update_todo(db: Session, todo_id: int, title: str, description: str, done: int):
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    if db_todo:
        db_todo.title = title
        db_todo.description = description
        db_todo.done = done
        db.commit()
        db.refresh(db_todo)
        return db_todo
    return None

# Delete a ToDo by ID
def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()
        return db_todo
    return None
