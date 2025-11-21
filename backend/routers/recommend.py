from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models import RoutineLog
from ai.analyzer import analyze_routines
from ai.recommender import suggest_productivity

router = APIRouter(prefix="/recommend", tags=["Recommendations"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.get("/")
def get_recommendations(db: Session = Depends(get_db)):
    routines = db.query(RoutineLog).all()
    analysis = analyze_routines(routines)
    suggestions = suggest_productivity(analysis)
    return {"analysis": analysis, "suggestions": suggestions}
