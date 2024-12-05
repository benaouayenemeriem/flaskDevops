from . import db
from app.models.user import User
from flask import jsonify

# Create User
def create_user(username, email, password_hash, role):
    new_user = User(username=username, email=email, password_hash=password_hash, role=role)
    db.session.add(new_user)
    db.session.commit()
    return new_user

# Get all Users
def get_all_users():
    users = User.query.all()
    return jsonify([user.username for user in users])

# Get User by ID
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({
            'username': user.username,
            'email': user.email,
            'created_at': user.created_at
        })
    return jsonify({'message': 'User not found'}), 404

# Update User
def update_user(user_id, username=None, email=None, password_hash=None, role=None):
    user = User.query.get(user_id)
    if user:
        if username:
            user.username = username
        if email:
            user.email = email
        if password_hash:
            user.password_hash = password_hash
        if role:
            user.role = role
        db.session.commit()
        return jsonify({'message': 'User updated successfully'})
    return jsonify({'message': 'User not found'}), 404

# Delete User
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'message': 'User not found'}), 404
