# Base image
FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    pkg-config \
    default-libmysqlclient-dev \
    build-essential \
    python3-dev \
    zlib1g-dev \
    libssl-dev

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Gunicorn 실행 설정 (마이그레이션 포함)
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && gunicorn --workers=2 --threads=2 --bind=0.0.0.0:8000 config.wsgi:application"]
