import sys
import os

script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(script_path))
sys.path.insert(0, project_root)
from app import app

if __name__ == "__main__":
    app.run(debug=True)
