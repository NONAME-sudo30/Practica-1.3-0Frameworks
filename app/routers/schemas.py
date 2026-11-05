from datetime import datetime
from pydantic import BaseModel, Field
# PROJECTS
class ProjectCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: str | None = None
class ProjectRead(ProjectCreate):
    id: int
    created_at: datetime
# TASKS
class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str | None = None
    project_id: int
class TaskRead(TaskCreate):
    id: int
    completed: bool
    created_at: datetime