
# Django URL Shortener

A clean, minimal **Django** URL shortener with a web UI + optional API.

## Features
- Create short links (auto or custom code)
- Redirect `/<code>` → original URL
- Track clicks + last accessed
- Clean Bootstrap UI
- Docker one-command start

## Quick Start (Local)
```bash
python -m venv venv
# Windows: venv\Scripts\activate
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
# open http://127.0.0.1:8000
```

## Docker (One Command)
```bash
docker compose up --build
# open http://127.0.0.1:8000
```

## URLs
- Home: `/` – shorten form
- Redirect: `/<code>` – follows to long URL
- Stats: `/stats/<code>` – simple metrics

## Project Structure
```
.
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── url_shortener/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── shortener/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations/
    ├── models.py
    ├── templates/
    │   └── shortener/
    │       ├── home.html
    │       └── stats.html
    └── views.py
```
