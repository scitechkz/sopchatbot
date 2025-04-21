# Use official Python runtime with slim variant
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Skip collectstatic if no database is configured
RUN if [ -z "$SKIP_COLLECTSTATIC" ]; then \
    python manage.py collectstatic --noinput --settings=sopchatbot.docker_settings || true; \
    fi

# Create a non-root user and switch to it
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Run gunicorn
CMD gunicorn \
    --bind 0.0.0.0:$PORT \
    --workers ${WEB_CONCURRENCY:-3} \
    --timeout ${GUNICORN_TIMEOUT:-120} \
    sopchatbot.wsgi:application