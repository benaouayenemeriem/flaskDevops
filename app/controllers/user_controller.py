from flask import request
from flask_restx import Namespace, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from app.services.user_service import create_user, get_all_users, get_user_by_id, update_user, delete_user

   
user_namespace = Namespace('users', description='User operations')


db = SQLAlchemy(app)

# Swagger model for User
user_model = user_namespace.model('User', {
    'username': fields.String(required=True, description='The user\'s username'),
    'email': fields.String(required=True, description='The user\'s email'),
    'password_hash': fields.String(required=True, description='The user\'s password hash'),
    'role': fields.String(required=True, description='The user\'s role')
})

# Define routes and resource classes
@user_namespace.route('/')
class UserList(Resource):
    def get(self):
        """Fetch all users"""
        return get_all_users(db)

    @user_namespace.expect(user_model)
    def post(self):
        """Create a new user"""
        data = request.get_json()
        user = create_user(db, data['username'], data['email'], data['password_hash'], data['role'])
        return {'message': 'User created successfully'}, 201

@user_namespace.route('/<int:user_id>')
class User(Resource):
    def get(self, user_id):
        """Fetch a user by ID"""
        return get_user_by_id(db, user_id)

    @user_namespace.expect(user_model)
    def put(self, user_id):
        """Update a user"""
        data = request.get_json()
        return update_user(db, user_id, **data)

    def delete(self, user_id):
        """Delete a user"""
        return delete_user(db, user_id)    
