from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.database import Base, engine
from backend.routers import tasks, routines, recommend
from backend.routers import llm_recommend

app = FastAPI()

# --- CORS FIX ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # allow all methods (GET, POST, DELETE, OPTIONS)
    allow_headers=["*"],  # allow all headers
)
# ------------------

Base.metadata.create_all(bind=engine)

app.include_router(llm_recommend.router)
app.include_router(tasks.router)
app.include_router(routines.router)
app.include_router(recommend.router)

@app.get("/")
def home():
    return {"message": "Backend + Database Ready!"}
