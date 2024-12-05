from . import db
from app.models.role import Role
from flask import jsonify

# Create Role
def create_role(name):
    new_role = Role(name=name)
    db.session.add(new_role)
    db.session.commit()
    return new_role

# Get all Roles
def get_all_roles():
    roles = Role.query.all()
    return jsonify([role.name for role in roles])

# Get Role by ID
def get_role_by_id(role_id):
    role = Role.query.get(role_id)
    if role:
        return jsonify({'name': role.name})
    return jsonify({'message': 'Role not found'}), 404

# Update Role
def update_role(role_id, name):
    role = Role.query.get(role_id)
    if role:
        role.name = name
        db.session.commit()
        return jsonify({'message': 'Role updated successfully'})
    return jsonify({'message': 'Role not found'}), 404

# Delete Role
def delete_role(role_id):
    role = Role.query.get(role_id)
    if role:
        db.session.delete(role)
        db.session.commit()
        return jsonify({'message': 'Role deleted successfully'})
    return jsonify({'message': 'Role not found'}), 404
