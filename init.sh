#!bin/bash
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser --username t18_admin --email jeongjooho1995@gmail.com