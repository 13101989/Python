#!usr/bin/env bash

PROJECT_BASE_PATH='/usr/local/apps/python_django_vagrant_aws'

sudo git pull origin main
$PROJECT_BASE_PATH/venv/bin/python $PROJECT_BASE_PATH/manage.py migrate
sudo $PROJECT_BASE_PATH/venv/bin/python $PROJECT_BASE_PATH/manage.py collectstatic --noinput
sudo supervisorctl restart profiles_api