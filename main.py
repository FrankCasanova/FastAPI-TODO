from fastapi import FastAPI

from fastapi.encoders import jsonable_encoder
from model.model import Task
import model.taskman as taskman

app = FastAPI()

@app.get('/api/tasks')
async def get_tasks():
    """
    Fetch the list of all tasks
    """ 
    return await taskman.get_tasks()


@app.get('/api/tasks/{id}')
async def get_task(id: int):
    """
    Fecht the task by id
    """
    return await taskman.get_tasks(id)


@app.post('/api/tasks/create')
async def create_task(task: Task):
    """
    1. Create a new task and
    2. Return the details of task
    """ 
    id = await taskman.create_task(task)
    return await taskman.get_tasks(id)
    


@app.put('/api/tasks/{id}/update')
async def update_task(id: int, task: Task):
    """
    1. Update the task by id
    2. Return the updated task

    Args:
        id (itn): [task id]
        task (Task): [instance of a Task]
    """
    await taskman.update_task(id, task)
    return await taskman.get_tasks(id)

@app.delete('/api/tasks/{id}/delete')
async def delete_task(id: int):
    """
    1. delete the task by id
    2. return a confimation of deletion

    Args:
        id (int): [id of a task that u desire to delete]
    """
    id = await taskman.delete_task(id)
    response = {id: 'Task successfully deleted'}
    return jsonable_encoder(response)
