from fastapi import FastAPI
from datetime import datetime
from typing import Optional

from fastapi.encoders import jsonable_encoder
from model.model import Task, TaskList
import model.taskman as taskman

app = FastAPI()

@app.get('/api/tasks')
async def get_task():
    """
    Fetch the list of all tasks
    """ 
    return 'TODO'


@app.get('/api/tasks/{id}')
async def get_task(id: int):
    """
    Fecht the task by id
    """
    return 'TODO'


@app.post('/api/tasks/create')
async def create_task(task: Task):
    """
    1. Create a new task and
    2. Return the details of task
    """ 
    return 'TODO'


@app.put('/api/tasks/{id}/update')
async def update_task(id: itn, task: Task):
    """
    1. Update the task by id
    2. Return the updated task

    Args:
        id (itn): [task id]
        task (Task): [instance of a Task]
    """
    return 'TODO'
