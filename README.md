# HRPlatformAPI
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/downloads/)
[![Django 5](https://img.shields.io/badge/django-5.0%2B-brightgreen)](https://www.djangoproject.com/)

Django REST API for HR platform: custom users, resume management and role-based permissions.

## Features
- Custom user model + token authentication
- Resume CRUD with file uploads support
- Separate apps: users, resumes
- Permission classes and serializers per app
- Ready for JWT / OAuth2 migration

## Stack
- Django 5 · DRF
- TokenAuthentication (easy switch to JWT)
- SQLite → PostgreSQL ready

## Run
```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
