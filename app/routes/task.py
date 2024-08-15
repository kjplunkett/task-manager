from flask import Blueprint, request

task_blueprint = Blueprint("task", __name__)

# In memory state
data = {}


@task_blueprint.route("/task", methods=["POST", "DELETE", "PUT"])
def task():
    """
    Handle task create, delete, and update operations
    """
    task_data = request.json

    if not task_data["id"]:
        return {"error": "Task ID is required"}, 400

    # Handle task create
    if request.method == "POST":
        data[task_data["id"]] = task_data
        return task_data, 201

    # Handle task update
    elif request.method == "PUT":
        data[task_data["id"]] = task_data
        return task_data, 200

    # Handle task delete
    elif request.method == "DELETE":
        del data[task_data["id"]]
        return "", 204


@task_blueprint.route("/tasks", methods=["GET"])
def tasks():
    """
    Display a list of tasks
    """
    return list(data.values()), 200
