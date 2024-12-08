from flask import request
from flask_restx import Namespace, Resource, fields
from main.services.task_service import create_task, get_all_tasks, get_task_by_id, update_task, delete_task
from ..config import db
from datetime import datetime

task_namespace = Namespace('tasks', description='Task operations')

# Swagger model for Task
task_model = task_namespace.model('Task', {
    'title': fields.String(required=True, description='The task\'s title'),
    'description': fields.String(required=False, description='The task\'s description'),
    'created_at': fields.DateTime(required=False, description='The task\'s creation time'),
    'due_date': fields.DateTime(required=False, description='The task\'s due date'),
    'user_id': fields.Integer(required=True, description='The ID of the user assigned to the task')
})

# Define routes and resource classes
@task_namespace.route('/')
class TaskList(Resource):
    def get(self):
        """Fetch all tasks"""
        return get_all_tasks(db)

    @task_namespace.expect(task_model)
    def post(self):
        """Create a new task"""
        data = request.get_json()
        # Ensure 'created_at' defaults to the current datetime if not provided
        if 'created_at' not in data:
            data['created_at'] = datetime.utcnow()
        task = create_task(db, data['title'], data['description'], data['created_at'], data['due_date'], data['user_id'])
        return {'message': 'Task created successfully'}, 201

@task_namespace.route('/<int:task_id>')
class Task(Resource):
    def get(self, task_id):
        """Fetch a task by ID"""
        return get_task_by_id(db, task_id)

    @task_namespace.expect(task_model)
    def put(self, task_id):
        """Update a task"""
        data = request.get_json()
        return update_task(db, task_id, **data)

    def delete(self, task_id):
        """Delete a task"""
        return delete_task(db, task_id)
