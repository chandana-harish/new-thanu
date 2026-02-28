from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from . import models
from .routes import employee, task, issue

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Task & Issue Management System")

# ✅ ADD THIS BLOCK (CORS FIX)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employee.router)
app.include_router(task.router)
app.include_router(issue.router)

@app.get("/")
def root():
    return {"message": "API is running successfully"}
