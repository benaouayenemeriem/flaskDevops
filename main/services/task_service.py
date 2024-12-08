from datetime import datetime
from main.models import Task

def create_task(db, title, description, due_date, user_id):
    """Create a new task"""
    new_task = Task(title=title, description=description, due_date=due_date, user_id=user_id)
    db.session.add(new_task)
    db.session.commit()
    return new_task

def get_all_tasks(db):
    """Fetch all tasks"""
    tasks = Task.query.all()
    return [{
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'created_at': task.created_at,
        'due_date': task.due_date,
        'user_id': task.user_id
    } for task in tasks]

def get_task_by_id(db, task_id):
    """Fetch a task by ID"""
    task = Task.query.get(task_id)
    if task:
        return {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'created_at': task.created_at,
            'due_date': task.due_date,
            'user_id': task.user_id
        }
    return {'message': 'Task not found'}, 404

def update_task(db, task_id, title, description, due_date, user_id):
    """Update a task"""
    task = Task.query.get(task_id)
    if task:
        task.title = title
        task.description = description
        task.due_date = due_date
        task.user_id = user_id
        db.session.commit()
        return {'message': 'Task updated successfully'}
    return {'message': 'Task not found'}, 404

def delete_task(db, task_id):
    """Delete a task"""
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return {'message': 'Task deleted successfully'}
    return {'message': 'Task not found'}, 404
