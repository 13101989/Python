from fastapi import FastAPI, HTTPException
from models import Task, TaskWithId, UpdateTask, TaskV2WithId
from operations import (
    read_all_tasks,
    read_task,
    create_task,
    modify_task,
    remove_task,
    read_all_tasks_v2,
)
from typing import Optional

app = FastAPI()


@app.get("/tasks/search", response_model=list[TaskWithId])
def search_tasks(keyword: str):
    tasks = read_all_tasks()
    filtered_tasks = [
        task
        for task in tasks
        if keyword.lower() in (task.title + task.description).lower()
    ]
    return filtered_tasks


@app.get("/tasks", response_model=list[TaskWithId])
def get_tasks(status: Optional[str] = None, title: Optional[str] = None):
    tasks = read_all_tasks()

    if status:
        tasks = [task for task in tasks if task.status == status]
    if title:
        tasks = [task for task in tasks if task.title == title]

    return tasks


@app.get("/v2/tasks", response_model=list[TaskV2WithId])
def get_tasks_v2():
    return read_all_tasks_v2()


@app.get("/tasks/{task_id}", response_model=TaskWithId)
def get_task(task_id: int):
    task = read_task(task_id)

    if not task:
        raise HTTPException(status_code=404, detail="task not found")

    return task


@app.post("/task", response_model=TaskWithId)
def add_task(task: Task):
    return create_task(task)


@app.put("/tasks/{task_id}", response_model=TaskWithId)
def update_task(task_id: int, task_update: UpdateTask):
    modified_task = modify_task(task_id, task_update.model_dump(exclude_unset=True))

    if not modified_task:
        raise HTTPException(status_code=404, detail="task not found")

    return modified_task


@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    removed_task = remove_task(task_id)

    if not removed_task:
        raise HTTPException(status_code=404, detail="task not found")

    return removed_task
