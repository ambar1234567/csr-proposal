from flask import Flask

# Create the Flask application instance
app = Flask(__name__)

# Import routes AFTER app creation to avoid circular imports
from app.routes import *
