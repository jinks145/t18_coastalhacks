FROM python:3.9

RUN adduser t18_admin 

ADD . /t18_todos

WORKDIR /t18_todos

COPY Pipfile ./

EXPOSE 8000

RUN pip install pipenv
RUN pipenv install --system

RUN chmod +x ./init.sh
