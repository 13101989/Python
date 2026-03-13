from pydantic import BaseModel
from typing import Optional


class Task(BaseModel):
    title: str
    description: str
    status: str


class TaskWithId(Task):
    id: int


class UpdateTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
