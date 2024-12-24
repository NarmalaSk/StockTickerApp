from app import app
from waitress import serve
import os

if __name__ == "__main__":
    # Use waitress to serve the application
    serve(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
