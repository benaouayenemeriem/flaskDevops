from flask import request
from flask_restx import Namespace, Resource, fields
from main.services.role_service import create_role, get_all_roles, get_role_by_id, update_role, delete_role
from ..config import db

role_namespace = Namespace('roles', description='Role operations')

# Swagger model for Role
role_model = role_namespace.model('Role', {
    'name': fields.String(required=True, description='The role\'s name')
})

# Define routes and resource classes
@role_namespace.route('/')
class RoleList(Resource):
    def get(self):
        """Fetch all roles"""
        return get_all_roles(db)

    @role_namespace.expect(role_model)
    def post(self):
        """Create a new role"""
        data = request.get_json()
        role = create_role(db, data['name'])
        return {'message': 'Role created successfully'}, 201

@role_namespace.route('/<int:role_id>')
class Role(Resource):
    def get(self, role_id):
        """Fetch a role by ID"""
        return get_role_by_id(db, role_id)

    @role_namespace.expect(role_model)
    def put(self, role_id):
        """Update a role"""
        data = request.get_json()
        return update_role(db, role_id, **data)

    def delete(self, role_id):
        """Delete a role"""
        return delete_role(db, role_id)
