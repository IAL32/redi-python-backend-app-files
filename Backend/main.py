from typing import Dict
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import os
import json

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Task(BaseModel):
    title: str
    description: str
    completed: bool
    due_date: str

# when the server starts, check if the file exists.
if not os.path.exists("tasks.json"):
    # if no file exists, create a new empty file
    file = open("tasks.json", "w")
    file.write("")
    # close the file
    file.close()

def read_all_tasks():
    """
    Reads all tasks from the file and returns
    them as a dictionary
    """
    file = open("tasks.json", "r")
    file_contents = file.read()
    if len(file_contents) == 0:
        # if the file is empty, return an empty
        # dictionary
        return {}
    # if the file is not empty, parse the JSON
    raw_json_data = json.loads(file_contents)

    # convert each task to a Pydantic model
    task_list: Dict[int, Task] = {}
    for task_id in raw_json_data:
        # convert each task to a Pydantic model
        # before returning
        task = Task(**raw_json_data[task_id])
        # add the task to the dictionary
        # with the task ID as the key
        task_list[int(task_id)] = task
    # close the file
    file.close()
    return task_list

def write_tasks(task_list: Dict[int, Task]):
    """
    Writes all tasks to the file from the given
    dictionary.
    """
    file = open("tasks.json", "w")
    for task_id in task_list:
        # convert each task to a dictionary
        # before writing to file (Pydantic
        # models are not serializable)
        task_list[task_id] = task_list[task_id].dict()
    file.write(json.dumps(task_list))
    file.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/tasks")
async def read_tasks():
    return read_all_tasks()

@app.post("/tasks")
async def create_task(task: Task):
    task_list = read_all_tasks()

    task_id = 0
    if len(task_list) == 0:
        task_id = 1
    else:
        task_id = max(task_list.keys()) + 1
    task_list[task_id] = task

    write_tasks(task_list)

    return {"task_id": task_id}

@app.get("/tasks/{task_id}")
async def read_task(task_id: int):
    task_list = read_all_tasks()
    if task_id not in task_list:
        return {"error": "Task not found"}
    return task_list[task_id]

@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    task_list = read_all_tasks()
    if task_id not in task_list:
        return {"error": "Task not found"}
    task_list[task_id] = task
    write_tasks(task_list)

    return {"message": "Task updated successfully"}

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    task_list = read_all_tasks()   

    if task_id not in task_list:
        return {"error": "Task not found"}
    del task_list[task_id]

    write_tasks(task_list)
    return {"message": "Task deleted successfully"}

if __name__ == "__main__":
    uvicorn.run("main:app",
                host='127.0.0.1',
                port=4557,
                reload=True,
                log_level="info")
