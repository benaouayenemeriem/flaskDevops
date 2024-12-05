from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.task_service import create_task, get_all_tasks, get_task_by_id, update_task, delete_task

api = Namespace('tasks', description='Task operations')

# Define Swagger model for Task
task_model = api.model('Task', {
    'title': fields.String(required=True, description='The title of the task'),
    'description': fields.String(required=True, description='The description of the task'),
    'due_date': fields.String(required=True, description='The due date of the task'),
    'user_id': fields.Integer(required=True, description='The ID of the user assigned to the task')
})

@api.route('/')
class TaskList(Resource):
    @api.doc('list_tasks')
    def get(self):
        """Fetch all tasks"""
        return get_all_tasks()

    @api.doc('create_task')
    @api.expect(task_model)
    def post(self):
        """Create a new task"""
        data = request.get_json()
        task = create_task(data['title'], data['description'], data['due_date'], data['user_id'])
        return {'message': 'Task created successfully'}, 201

@api.route('/<int:task_id>')
class Task(Resource):
    @api.doc('get_task')
    def get(self, task_id):
        """Fetch a task by ID"""
        return get_task_by_id(task_id)

    @api.doc('update_task')
    @api.expect(task_model)
    def put(self, task_id):
        """Update a task"""
        data = request.get_json()
        return update_task(task_id, **data)

    @api.doc('delete_task')
    def delete(self, task_id):
        """Delete a task"""
        return delete_task(task_id)
