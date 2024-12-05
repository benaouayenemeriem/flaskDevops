from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.role_service import create_role, get_all_roles, get_role_by_id, update_role, delete_role

api = Namespace('roles', description='Role operations')

# Define Swagger model for Role
role_model = api.model('Role', {
    'name': fields.String(required=True, description='The name of the role')
})

@api.route('/')
class RoleList(Resource):
    @api.doc('list_roles')
    def get(self):
        """Fetch all roles"""
        return get_all_roles()

    @api.doc('create_role')
    @api.expect(role_model)
    def post(self):
        """Create a new role"""
        data = request.get_json()
        role = create_role(data['name'])
        return {'message': 'Role created successfully'}, 201

@api.route('/<int:role_id>')
class Role(Resource):
    @api.doc('get_role')
    def get(self, role_id):
        """Fetch a role by ID"""
        return get_role_by_id(role_id)

    @api.doc('update_role')
    @api.expect(role_model)
    def put(self, role_id):
        """Update a role"""
        data = request.get_json()
        return update_role(role_id, **data)

    @api.doc('delete_role')
    def delete(self, role_id):
        """Delete a role"""
        return delete_role(role_id)
