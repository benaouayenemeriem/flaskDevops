from app import create_app
from app.config import Config

# Create the Flask app instance
app = create_app()
app.config.from_object(Config)

@app.route('/')
def home():
    return "Hello, World! Flask App is running!"

from flask import Flask
from flask_restx import Api
from app.controllers.user_controller import api as user_api
from app.controllers.task_controller import api as task_api
from app.controllers.role_controller import api as role_api

# Initialize Flask app
app = Flask(__name__)

# Initialize API for Flask-RESTPlus (Swagger)
api = Api(app, version='1.0', title='Flask API', description='A simple Flask API')

# Register the namespaces (controllers)
api.add_namespace(user_api, path='/users')
api.add_namespace(task_api, path='/tasks')
api.add_namespace(role_api, path='/roles')


api.add_namespace(user_namespace)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
