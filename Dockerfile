# Use an official Python base image compatible with amd64
FROM --platform=linux/amd64 python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the required files into the container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set entrypoint to run the script
ENTRYPOINT ["python", "process_collection.py"]
