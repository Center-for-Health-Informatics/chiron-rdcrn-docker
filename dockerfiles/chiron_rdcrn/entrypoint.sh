#!/bin/sh

rm db.sqlite3
rm staging.sqlite3

python dockermanage.py makemigrations usermanager
python dockermanage.py migrate
python dockermanage.py migrate --database=staging
python dockermanage.py redcap_restore_dd
python dockermanage.py chiron_restore_dd
python dockermanage.py collectstatic --no-input

gunicorn project.wsgi_docker:application --bind 0.0.0.0:8000