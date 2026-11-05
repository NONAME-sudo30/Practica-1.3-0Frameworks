from fastapi import APIRouter
from app.task import router as task_router
from app.proyect import router as proyect_router
app= fastAPI()
app.include_router(task_router)
app.include_router(proyect_router)