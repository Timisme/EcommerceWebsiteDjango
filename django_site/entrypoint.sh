#!/bin/sh

echo 'Run migration'
# python manage.py makemigrations
python manage.py migrate --no-input

echo 'Collect Static'
# python manage.py collectstatic --no-input

exec "$@"
# python manage.py runserver 0.0.0.0:8080

