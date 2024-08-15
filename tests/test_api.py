def test_tasks_get(client):
    """
    Test listing tasks
    """
    res = client.get("/tasks")
    data = res.json
    assert data == []
    assert res.status_code == 200


def test_task_post(client):
    """
    Test creating a new task
    """
    # Assert we have 0 tasks to start
    all_tasks = client.get("/tasks").json
    assert len(all_tasks) == 0

    # Create a task
    task = {
        "id": "1",
        "title": "foo",
        "description": "bar",
        "completed": False,
    }
    res = client.post("/task", json=task)

    # Assert the response is 201 created and the task data is returned
    assert res.status_code == 201
    assert res.json == task

    # Assert we have 1 task now
    all_tasks = client.get("/tasks").json
    assert len(all_tasks) == 1


def test_task_put(client):
    """
    Test updating a task
    """
    # Create a task
    task = {
        "id": "1",
        "title": "foo",
        "description": "bar",
        "completed": False,
    }
    client.post("/task", json=task)

    # Assert we have 1 task
    all_tasks = client.get("/tasks").json
    assert len(all_tasks) == 1

    # Update the task title
    task["title"] = "buz"
    res = client.put("/task", json=task)

    # Assert the response is 200 and the updated task is returned
    assert res.status_code == 200
    assert res.json == task

    # Assert only the updated task exists
    all_tasks = client.get("/tasks").json
    assert all_tasks == [task]


def test_task_delete(client):
    """
    Test deleting a task
    """
    # Create a task
    task = {
        "id": "1",
        "title": "foo",
        "description": "bar",
        "completed": False,
    }
    client.post("/task", json=task)

    # Assert we have 1 task
    all_tasks = client.get("/tasks").json
    assert len(all_tasks) == 1

    # Delete the task
    res = client.delete("/task", json={"id": "1"})

    # Assert we get an empty 204 response
    assert res.status_code == 204
    assert res.json is None

    # Assert we have 0 tasks left
    all_tasks = client.get("/tasks").json
    assert len(all_tasks) == 0
