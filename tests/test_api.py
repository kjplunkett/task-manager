def test_tasks_get(client):
    """
    Test listing no tasks
    """
    res = client.get("/tasks")
    data = res.json

    assert data == []
    assert res.status_code == 200


def test_task_post(client):
    """
    Test creating a new task
    """
    # Create a task
    task = {
        "title": "foo",
        "description": "bar",
    }
    res = client.post("/task", json=task)

    # Assert the response is 201 created and the new task data is returned
    new_task = res.json
    assert res.status_code == 201
    assert new_task['id'] == 1
    assert new_task['title'] == 'foo'
    assert new_task['description'] == 'bar'
    assert new_task['completed'] == False

    # Assert we have 1 task now
    all_tasks = client.get("/tasks").json
    assert len(all_tasks) == 1


def test_task_put(client):
    """
    Test updating a task
    """
    # Create a task
    task = {
        "title": "fiz",
        "description": "buz",
    }
    res = client.post("/task", json=task)
    task_id = res.json['id']

    # Update the task title
    task["title"] = "new title"
    res = client.put(f"/task/{task_id}", json=task)

    # Assert the title was updated
    assert res.status_code == 200
    assert res.json['title'] == 'new title'


def test_task_delete(client):
    """
    Test deleting a task
    """
    # Create a task
    task = {
        "title": "hello",
        "description": "world",
    }
    res =client.post("/task", json=task)
    task_id = res.json['id']

    # Assert we have 1 task
    all_tasks = client.get("/tasks").json
    assert len(all_tasks) == 1

    # Delete the task
    res = client.delete(f"/task/{task_id}")

    # Assert we get an empty 204 response
    assert res.status_code == 204
    assert res.json is None

    # Assert we have 0 tasks left
    all_tasks = client.get("/tasks").json
    assert len(all_tasks) == 0
