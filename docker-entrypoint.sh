#!/bin/bash
pipenv install
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
chmod 777 media
# Dev Or Product

if $DOCKER_DEV
then
    pipenv run python manage.py runserver 0.0.0.0:8000
else
    pipenv run python manage.py collectstatic --noinput
    # uwsgi --ini uwsgi.ini
    NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program uwsgi --ini uwsgi.ini
fi
