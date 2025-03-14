# Use an official lightweight Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy required files into the container
COPY requirements.txt .
COPY app.py .
COPY model.h5 .
COPY templates/ templates/
COPY static/ static/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ensure the uploads folder exists inside the container
RUN mkdir -p static/uploads && chmod -R 777 static/uploads

# Expose port 8000 for FastAPI
EXPOSE 8000

# Run FastAPI with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]


