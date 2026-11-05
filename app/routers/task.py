from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Task

router = APIRouter(prefix="/tasks", tags=["tasks"])


class TaskIn(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
    project_id: int


class TaskOut(TaskIn):
    id: int

    class Config:
        from_attributes = True


@router.get("", response_model=list[TaskOut])
def list_tasks(project_id: Optional[int] = None, completed: Optional[bool] = None,
               skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    query = db.query(Task)
    if project_id is not None:
        query = query.filter(Task.project_id == project_id)
    if completed is not None:
        query = query.filter(Task.completed == completed)
    return query.offset(skip).limit(limit).all()


@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(404, "Tarea no encontrada")
    return task


@router.post("", response_model=TaskOut, status_code=201)
def create_task(data: TaskIn, db: Session = Depends(get_db)):
    task = Task(**data.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.put("/{task_id}", response_model=TaskOut)
def update_task(task_id: int, data: TaskIn, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(404, "Tarea no encontrada")
    for key, value in data.model_dump().items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task


@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(404, "Tarea no encontrada")
    db.delete(task)
    db.commit()