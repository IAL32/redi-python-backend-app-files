from typing import Dict
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

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

task_list: Dict[int, Task] = {}

@app.get("/")
async def root():
    return {"message": "Hello World"}

# @app. """Add the appropriate REST verb (GET, POST, PUT, DELETE)"""
# async def read_tasks():
#     """
#     Returns a JSON response containing a list of all tasks.
#     """
#     pass

# @app. """Add the appropriate REST verb (GET, POST, PUT, DELETE)"""
# async def create_task("""Add the appropriate input argument"""):
#     """
#     Accepts a JSON request body containing details of a new task and adds it to the list of tasks.
#     Returns a JSON response containing the ID of the newly created task.
#     """
#     pass

# @app. "Add the appropriate REST verb (GET, POST, PUT, DELETE)"
# async def read_task("""Add the appropriate input argument"""):
#     """
#     Accepts an integer `task_id` as a path parameter and returns details of the task with that ID.
#     If no task is found with that ID, returns a JSON response containing an error message.
#     """
#     pass

# @app "Add the appropriate REST verb (GET, POST, PUT, DELETE)"
# async def update_task("""Add the appropriate input argument"""):
#     """
#     Accepts an integer `task_id` as a path parameter and a JSON request body containing updated details for that task.
#     Updates the details of the task with that ID in the list of tasks.
#     If no task is found with that ID, returns a JSON response containing an error message.
#     Returns a JSON response containing a message to indicate that the task was updated successfully.
#     """
#     pass

# @app. "Add the appropriate REST verb (GET, POST, PUT, DELETE)"
# async def delete_task("""Add the appropriate input argument"""):    
#     """
#     Accepts an integer `task_id` as a path parameter and deletes the task with that ID from the list of tasks.
#     If no task is found with that ID, returns a JSON response containing an error message.
#     Returns a JSON response containing a message to indicate that the task was deleted successfully.
#     """
#     pass

if __name__ == "__main__":
    uvicorn.run("main:app",
                host='127.0.0.1',
                port=4557,
                reload=True,
                log_level="info")
