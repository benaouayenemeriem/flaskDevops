from . import db
from app.models.task import Task
from flask import jsonify

# Create Task
def create_task(title, description, due_date, user_id):
    new_task = Task(title=title, description=description, due_date=due_date, user_id=user_id)
    db.session.add(new_task)
    db.session.commit()
    return new_task

# Get all Tasks
def get_all_tasks():
    tasks = Task.query.all()
    return jsonify([task.title for task in tasks])

# Get Task by ID
def get_task_by_id(task_id):
    task = Task.query.get(task_id)
    if task:
        return jsonify({
            'title': task.title,
            'description': task.description,
            'due_date': task.due_date
        })
    return jsonify({'message': 'Task not found'}), 404

# Update Task
def update_task(task_id, title=None, description=None, due_date=None, user_id=None):
    task = Task.query.get(task_id)
    if task:
        if title:
            task.title = title
        if description:
            task.description = description
        if due_date:
            task.due_date = due_date
        if user_id:
            task.user_id = user_id
        db.session.commit()
        return jsonify({'message': 'Task updated successfully'})
    return jsonify({'message': 'Task not found'}), 404

# Delete Task
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted successfully'})
    return jsonify({'message': 'Task not found'}), 404
