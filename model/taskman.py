from model.model import Task, TaskList
import json
from pydantic import parse_file_as
from typing import List, Optional

filepath = 'data/tasks.json'

async def data_to_json(data: list):
    """
    1. Take input data, of a list of tasks.
    2. Write the data into a json file (tasks.json)
    

    Args:
        data (list): [list of tasks]
    """
    data = json.dumps(data)
    with open(filepath, 'w') as file:
        file.write(data)


async def get_tasks(id: Optional[int] = 0):
    """
    1. Fetch all tasks if not argument (id) provided.
    2. Else fetch the task by id provided

    Args:
        id (Optional[int], optional): [id of a task]. Defaults to 0.
    """
    tasks = parse_file_as(List[TaskList], "data/tasks.json")
    data = {task.id: task.dict() for task in tasks}
    try:
        response = data if id == 0 else data[id]
    except: 
        response = 'Does not exist any task with that ID' 
    return response


async def create_task(new_task: Task):
    """
    1. Create a new task and add it ot the list of tasks
    2. Write the update tasklist to file

    Args:
        new_task (Task): [Task object from model]
    """
    tasks = parse_file_as(List[TaskList], 'data/tasks.json')
    id = max([task.id for task in tasks]) + 1
    tasks.append(TaskList(id=id, task=new_task))
    data = [task.dict() for task in tasks]
    await data_to_json(data)
    return id

async def delete_task(id):
    """
    1. Delete the task by id provided

    Args:
        id ([type]): [id of a task]
    """
    tasks = parse_file_as(List[TaskList], 'data/tasks.json')
    tasks = [task for task in tasks if task.id != id]
    data = [task.dict() for task in tasks]
    await data_to_json(data)
    return id

async def update_task(id: int, new_task: Task):
    """
    1. Update the task by id based on new task details
    2, write the updated taslikst to file

    Args:
        id (int): [id of a task that desire update]
        new_task (Task): [task objec that override the old task]
    """
    tasks = parse_file_as(List[TaskList], "data/tasks.json")
    data = [task.dict() for task in tasks]
    for task in data:
        if task["id"] == id:
            task["task"] = new_task.dict()

    await data_to_json(data)

    return id
    