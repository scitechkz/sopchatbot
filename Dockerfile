# Use an official Python runtime as a base image
FROM python:3.11

# Set environment variables (important for Django in production)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies (Postgres client libraries needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy and install Python dependencies first (for caching)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . /app/

# (Optional) Don't collect static files inside the Dockerfile
# Instead, let Render run collectstatic in postDeploy
# RUN python manage.py collectstatic --noinput --clear || echo "Static collection failed"

# Expose the port (Render automatically sets $PORT)
EXPOSE 8000

# Run Gunicorn, using $PORT environment variable
CMD gunicorn sopchatbot.wsgi:application --bind 0.0.0.0:8000 --workers 1 --timeout 600

