#!/bin/sh
python django/manage.py makemigrations --noinput
python django/manage.py migrate --noinput
python django/manage.py collectstatic --noinput

gunicorn --chdir ./django sns.wsgi:application --bind 0.0.0.0:8000
