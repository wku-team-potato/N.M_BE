# Python 베이스 이미지 사용
FROM python:3.9.13

# 작업 디렉토리 설정
WORKDIR /app

# 종속성 파일 복사
COPY requirements.txt /app/

# 종속성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . /app/

# Gunicorn 실행 설정 (마이그레이션 포함)
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && gunicorn --workers=2 --threads=2 --bind=0.0.0.0:8000 config.wsgi:application"]
