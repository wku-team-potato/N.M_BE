# Python
FROM python:3.9.13

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["nohup", "python", "manage.py", "runserver", "0.0.0.0:8000"]