from sqlalchemy import Column, Integer, String,DateTime
from backend.database import Base
from datetime import datetime
from pydantic import BaseModel

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    deadline = Column(String, nullable=True)
    priority = Column(Integer, default=1)
    status = Column(String, default="pending")

class RoutineLog(Base):
    __tablename__ = "routine_logs"

    id = Column(Integer, primary_key=True, index=True)
    activity = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)  # duration in minutes
    timestamp = Column(DateTime, default=datetime.utcnow)
class TaskCreate(BaseModel):
    title: str
    deadline: str | None = None
    priority: int = 1
class RoutineCreate(BaseModel):
    activity: str
    duration: int  # duration in minutes
    
  
