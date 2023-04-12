from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_task():
    """
    Test the create_task endpoint by sending a POST request with a Task object as the body.
    Verify that the endpoint returns a JSON response with a 'task_id' key and that the task is added to the task_list.
    """
    pass  # replace with test code

def test_read_task():
    """
    Test the read_task endpoint by sending a GET request with a task_id as a path parameter.
    Verify that the endpoint returns a JSON response with the correct task object.
    """
    pass  # replace with test code

def test_read_tasks():
    """
    Test the read_tasks endpoint by sending a GET request.
    Verify that the endpoint returns a JSON response with all tasks in the task_list.
    """
    pass  # replace with test code

def test_update_task():
    """
    Test the update_task endpoint by sending a PUT request with a task_id and a Task object as the body.
    Verify that the endpoint returns a JSON response with a 'message' key and that the task is updated in the task_list.
    """
    pass  # replace with test code

def test_delete_task():
    """
    Test the delete_task endpoint by sending a DELETE request with a task_id as a path parameter.
    Verify that the endpoint returns a JSON response with a 'message' key and that the task is deleted from the task_list.
    """
    pass  # replace with test code
