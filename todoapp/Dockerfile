# Base Image
FROM python:3.10-slim

# Environment variables:
# 1 Prevents from writing .pyc files
# 2 Ensures that python show real-time output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt requirements.txt

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code to the same directory
COPY . .

# Command to run Django app
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
