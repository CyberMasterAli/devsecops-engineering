# 1. Use a minimal, secure base image
FROM python:3.10-alpine

# 2. Prevent Python from writing .pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Create a non-root user for security
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# 4. Set working directory
WORKDIR /app

# 5. Install dependencies securely
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy application code and set ownership to the non-root user
COPY --chown=appuser:appgroup . .

# 7. Switch to the non-root user
USER appuser

# 8. Expose a non-privileged port (Ports under 1024 require root)
EXPOSE 8080

# 9. Run the application
CMD ["python", "app.py"]