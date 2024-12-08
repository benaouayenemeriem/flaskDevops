from main.models import Role

def create_role(db, name):
    """Create a new role"""
    new_role = Role(name=name)
    db.session.add(new_role)
    db.session.commit()
    return new_role

def get_all_roles(db):
    """Fetch all roles"""
    roles = Role.query.all()
    return [{'id': role.id, 'name': role.name} for role in roles]

def get_role_by_id(db, role_id):
    """Fetch a role by ID"""
    role = Role.query.get(role_id)
    if role:
        return {'id': role.id, 'name': role.name}
    return {'message': 'Role not found'}, 404

def update_role(db, role_id, name):
    """Update a role"""
    role = Role.query.get(role_id)
    if role:
        role.name = name
        db.session.commit()
        return {'message': 'Role updated successfully'}
    return {'message': 'Role not found'}, 404

def delete_role(db, role_id):
    """Delete a role"""
    role = Role.query.get(role_id)
    if role:
        db.session.delete(role)
        db.session.commit()
        return {'message': 'Role deleted successfully'}
    return {'message': 'Role not found'}, 404
