# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Set work directory
WORKDIR /app

# Install system dependencies required for psycopg2
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    postgresql-client \
    libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requiremts.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requiremts.txt

# Copy application code
COPY . .

# Create a non-root user to run the application
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose port


# Run the application
CMD ["uvicorn", "main:app"]
