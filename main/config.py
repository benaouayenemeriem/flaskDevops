from flask_sqlalchemy import SQLAlchemy

# Create the SQLAlchemy object
db = SQLAlchemy()

def initialize_db(app):
    """Initialize the database with the app."""
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:example@mysql:3306/mydatabase'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Import models after initializing the db to avoid circular imports
    from main.models import Task, Role, User
    
    db.init_app(app)

    

    # Create all tables within the app context
    with app.app_context():
        try:
            print("Creating tables...")
            db.create_all()  # Create all tables defined in the models
            print("Tables created successfully.")
        except Exception as e:
            print(f"Error creating tables: {e}")
    