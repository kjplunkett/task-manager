from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from app.db.models import Task


class TaskSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        load_instance = True
