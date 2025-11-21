from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models import Task, TaskCreate

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/add")
def add_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(
        title=task.title,
        deadline=task.deadline,
        priority=task.priority
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"message": "Task added", "task": new_task}
@router.get("/list")
def list_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return {"tasks": tasks}
@router.delete("/delete/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return {"message": "Task not found"}
    db.delete(task)
    db.commit()
    return {"message": "Task deleted"}