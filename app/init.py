from flask import Flask

# Create the Flask app instance
app = Flask(__name__)

# Import routes AFTER creating app to avoid circular imports
from app import routes  # This must come last
