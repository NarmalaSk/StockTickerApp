from app import app
from waitress import serve
import os

if __name__ == "__main__":
    # Use waitress for local development
    if os.getenv("FLASK_ENV") == "development":
        serve(app, host='127.0.0.1', port=8080)
    else:
        # You can use gunicorn for production deployment, but it's handled by the platform
        app.run(host='0.0.0.0', port=8080)
