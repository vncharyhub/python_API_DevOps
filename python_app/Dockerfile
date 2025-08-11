# 1. Use Python base image
FROM python:3.10-slim

# 2. Set working directory in the container
WORKDIR /app

# 3. Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy application code
COPY app.py .

# 5. Expose port
EXPOSE 5000

# 6. Command to run the app
CMD ["python", "app.py"]
