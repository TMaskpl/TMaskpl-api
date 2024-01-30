#!/bin/bash

source /tmaskpl/.env
python manage.py makemigrations
python manage.py migrate
DJANGO_SUPERUSER_USERNAME=$DJANGO_SUPERUSER_USERNAME
DJANGO_SUPERUSER_PASSWORD=$DJANGO_SUPERUSER_PASSWORD
DJANGO_SUPERUSER_EMAIL=$DJANGO_SUPERUSER_EMAIL
python manage.py createsuperuser --noinput
python manage.py runserver 0.0.0.0:8000