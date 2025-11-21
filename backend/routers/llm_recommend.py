from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models import RoutineLog
from ai.llm_recommend import analyze_with_llm

router = APIRouter(prefix="/llm", tags=["LLM Recommendations"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/recommend")
def get_llm_recommendations(db: Session = Depends(get_db)):
    routines = db.query(RoutineLog).all()
    result = analyze_with_llm(routines)
    return {"ai_analysis": result}
