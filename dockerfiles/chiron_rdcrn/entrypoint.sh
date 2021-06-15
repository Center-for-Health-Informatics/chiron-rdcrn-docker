#!/bin/sh

rm db.sqlite3
rm staging.sqlite3

python manage.py makemigrations user_manager
python manage.py migrate
python manage.py redcap_restore_dd
python manage.py chiron_restore_dd
python manage.py collectstatic --no-input

gunicorn project.wsgi:application --bind 0.0.0.0:8000