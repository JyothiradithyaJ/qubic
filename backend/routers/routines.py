from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models import RoutineLog, RoutineCreate

router=APIRouter(prefix="/routine", tags=["Routine Logs"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post("/add")
def add_routine(entry: RoutineCreate, db: Session = Depends(get_db)):
    new_entry = RoutineLog(
        activity=entry.activity,
        duration=entry.duration
    )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return {"message": "Routine log added", "entry": new_entry}
@router.get("/list")
def list_routines(db: Session = Depends(get_db)):
    data = db.query(RoutineLog).all()
    return {"routine_logs": data}
@router.delete("/delete/{entry_id}")
def delete_routine(entry_id: int, db: Session = Depends(get_db)):
    item = db.query(RoutineLog).filter(RoutineLog.id == entry_id).first()
    if not item:
        return {"message": "entry not found"}
    db.delete(item)
    db.commit()
    return {"message": "Routine entry deleted"}