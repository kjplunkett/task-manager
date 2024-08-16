from flask import Blueprint, request

from app import db
from app.db.models import Task
from app.schemas.task import TaskSchema

task_blueprint = Blueprint("task", __name__)
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


@task_blueprint.route("/task", methods=["POST"])
def create_task():
    """
    Create a new task and return it
    """
    # Get the data from the request body
    task_data = request.json

    # Create a DB session
    session = db.session()

    # Serialize the task_data into a model instance (performs schema validation)
    task_instance = task_schema.load(task_data, session=session)

    # Persist the task instance to the db
    session.add(task_instance)
    session.commit()

    # Refresh the task instance in memory with the newly persisted task
    session.refresh(task_instance)

    # Deserialize the task into a dictionary
    task_response = task_schema.dump(task_instance)

    # Return the task with HTTP 201 Created
    return task_response, 201

@task_blueprint.route("/task/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    """
    Update an existing task and return it
    """
    # Get the data from the request body
    task_data = request.json

    # Create a DB session
    session = db.session()

    # Lookup an existing task by task_id
    task_instance = session.query(Task).filter(Task.id == task_id).first()

    # Handle no existing task with that id found
    if not task_instance:
        error_message = {'message': f'Task ID: {task_id} not found.'}
        return error_message, 404

    # Serialize the task_data into a new model instance
    updated_task_instance = task_schema.load(
        task_data,
        session=session,
        instance=task_instance
    )

    # Persist the new instance to the db
    session.commit()

    # Refresh the session with the updated task instance db state
    session.refresh(updated_task_instance)

    # Deserialize the task instance into a dict
    task_response = task_schema.dump(updated_task_instance)

    # Return the task with HTTP 200 Success
    return task_response, 200

@task_blueprint.route("/task/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """
    Delete an existing task
    """
    # Create a DB session
    session = db.session()

    # Serialize the task_data into a model instance (performs schema validation)
    task_instance = session.query(Task).filter(Task.id == task_id).first()

    # Handle no existing task with that id found
    if not task_instance:
        error_message = {'message': f'Task ID: {task_id} not found.'}
        return error_message, 404

    # Delete the task from the db
    session.delete(task_instance)
    session.commit()

    # Return no content HTTP 204
    return '', 204

@task_blueprint.route("/tasks", methods=["GET"])
def list_tasks():
    """
    Display a list of tasks
    """
    all_tasks = db.session.query(Task).all()

    return tasks_schema.dump(all_tasks), 200
