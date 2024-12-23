from app import app
from waitress import serve
import os

if __name__ == "__main__":
    # Use waitress for local development and production
    serve(app, host='0.0.0.0', port=8080)
