import sys
import os

script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(script_path))
sys.path.insert(0, project_root)

from flask import Flask
from sqlalchemy import create_engine
from config.config import DATABASE_URI

# Initialize the Flask app
app = Flask(__name__)

# Set up the SQLAlchemy engine
engine = create_engine(DATABASE_URI)

# Import routes after initializing the app and engine
from app import routes
