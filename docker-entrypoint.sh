#!/bin/bash
if [ ! -e env ]
then
  python -m pip install --user virtualenv
  virtualenv --python=python3.8 env
fi
source env/bin/activate

pip3 install -r requirements.txt -c constraints.txt
python3 manage.py makemigrations --no-input
python3 manage.py migrate --no-input
python3 manage.py runscript scripts.init
chmod 777 media
# Dev Or Product

python3 manage.py shell_plus --notebook &
if $DOCKER_DEV
then
    python3 manage.py runserver 0.0.0.0:8000
else
    python3 manage.py collectstatic --noinput
    # uwsgi --ini uwsgi.ini
    NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program uwsgi --ini uwsgi.ini
fi
