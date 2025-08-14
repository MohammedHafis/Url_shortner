FROM python:3.11-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
ENV DJANGO_SETTINGS_MODULE=url_shortener.settings
CMD bash -lc "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
