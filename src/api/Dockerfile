# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on (FastAPI default is 8000, but you can adjust as needed)
EXPOSE 8080

# Define environment variable to tell Uvicorn to run on port 80, if needed.
# CMD will run the Uvicorn server on container start.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", '--workers', "2"]
