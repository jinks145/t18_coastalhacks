#!/bin/bash
pipenv install
pipenv shell
python3 manage.py makemigrations --no-input
python3 manage.py migrate --no-input
chmod 777 media
# Dev Or Product

if $DOCKER_DEV
then
    python manage.py runserver 0.0.0.0:8000
else
    python3 manage.py collectstatic --noinput
    # uwsgi --ini uwsgi.ini
    NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program uwsgi --ini uwsgi.ini
fi
