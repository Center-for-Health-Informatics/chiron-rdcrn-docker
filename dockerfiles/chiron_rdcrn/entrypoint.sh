#!/bin/sh

rm db.sqlite3
rm staging.sqlite3

python manage.py makemigrations usermanager
python manage.py migrate
python manage.py redcap_restore_dd
python manage.py chiron_restore_dd
python manage.py collectstatic --no-input --settings=project.settings_docker

gunicorn project.wsgi_docker:application --bind 0.0.0.0:8000