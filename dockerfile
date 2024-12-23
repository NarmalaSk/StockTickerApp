# Use a base image with Python
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy your application files into the container
COPY . .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Cloud Run will use
EXPOSE 8080

# Set the default command to run your app (with Gunicorn or Waitress)
 web: gunicorn app:app
