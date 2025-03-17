from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

# Create the FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/todos")
def get_todos():
    return {"todos": ["todo1", "todo2", "todo3"]}


# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to get all todos
@app.get("/todos", response_model=list[schemas.ToDoBase])
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_todos(db, skip=skip, limit=limit)

# Route to create a new todo
@app.post("/todos", response_model=schemas.ToDoBase)
def create_todo(todo: schemas.ToDoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, title=todo.title, description=todo.description)

# Route to get a single todo by ID
@app.get("/todos/{todo_id}", response_model=schemas.ToDoBase)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo_by_id(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

# Route to update a todo
@app.put("/todos/{todo_id}", response_model=schemas.ToDoBase)
def update_todo(todo_id: int, todo: schemas.ToDoCreate, db: Session = Depends(get_db)):
    db_todo = crud.update_todo(db, todo_id=todo_id, title=todo.title, description=todo.description, done=0)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

# Route to delete a todo
@app.delete("/todos/{todo_id}", response_model=schemas.ToDoBase)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.delete_todo(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

if __name__ == "__main__":
    # Create the database tables
    models.Base.metadata.create_all(bind=database.engine)
