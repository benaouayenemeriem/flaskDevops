from flask import Flask, app
from flask_restx import Api
from main.config import initialize_db
from main.controllers.role_controller import role_namespace
from main.controllers.task_controller import task_namespace
from main.controllers.user_controller import user_namespace


app = Flask(__name__)
# Initialize Swagger and Database
api = Api(app, title="User Management API", version="1.0", description="APIs for User operations")
initialize_db(app)

@app.route('/')
def home():
    return "Hello, World! Flask App is running!"

# Register Namespaces
api.add_namespace(role_namespace, path="/role")
api.add_namespace(task_namespace, path="/task")
api.add_namespace(user_namespace, path="/user")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


