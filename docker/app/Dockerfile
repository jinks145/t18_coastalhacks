FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV SHELL /bin/bash
ENV DOCKER_DEV true

RUN apt-get update \
    # dependencies for building Python packages
    # && apt-get install -y build-essential \
    # psycopg2 dependencies
    && apt-get install -y libpq-dev 
RUN apt-get update \ 
    && apt-get install -y  virtualenv pipenv \
    # cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /root/.cache

RUN apt-get update\
    && apt-get install -y  build-essential

RUN useradd -m docker

RUN echo "docker ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

#USER docker

RUN mkdir -p /home/docker/app/

WORKDIR /home/docker/app

ENTRYPOINT ["/home/docker/app/docker-entrypoint.sh"]
