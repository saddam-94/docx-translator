# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /translator

# Copy the requirements file into the container
COPY requirements.txt .
# # Copy a local directory to a directory inside the container
# COPY ./Input_docx /Input_docx

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Define the command to run the application
CMD ["python", "translate.py"]