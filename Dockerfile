# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements if needed (empty for now)
COPY requirements.txt .

# Install dependencies (none for now)
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY ./src /app

# Default command
CMD ["python", "main.py"]