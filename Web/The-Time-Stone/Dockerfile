# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the working directory contents into the container at /app
COPY . /app

# Expose port 80 for the Flask app to be accessible
EXPOSE 80

# Define environment variable to ensure Flask runs in production
ENV FLASK_ENV=production

# Command to run the Flask application
CMD ["python", "app.py"]
