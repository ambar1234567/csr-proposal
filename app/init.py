from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Import routes AFTER app creation
    from app import routes
    routes.init_app(app)
    
    return app

# Create app instance
app = create_app()
