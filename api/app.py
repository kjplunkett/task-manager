from flask import Flask, request, make_response

app = Flask(__name__)

data = {}


@app.route("/tasks", methods=["GET"])
def tasks():
    """
    Display a list of tasks
    """
    return list(data.values()), 200


@app.route("/task", methods=["POST", "DELETE", "PUT"])
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
        return make_response("", 204)
