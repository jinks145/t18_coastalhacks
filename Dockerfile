FROM python:3.9

RUN adduser t18_admin 

ADD . /t18_repo

WORKDIR /t18_repo

COPY Pipfile ./

EXPOSE 8000

RUN pip install pipenv
RUN pipenv install --system

# RUN chmod +x ./init.sh
