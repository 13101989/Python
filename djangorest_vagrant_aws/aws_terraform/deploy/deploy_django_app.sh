#!/usr/bin/env bash

PROJECT_GIT_URL='https://github.com/13101989/python_django_vagrant_aws.git'
PROJECT_BASE_PATH='/usr/local/apps/python_django_vagrant_aws'

sudo echo "Installing dependencies..."
sudo apt-get update
sudo apt-get install -y python3-dev python3-venv python3-pip sqlite supervisor nginx git

# Create project directory and clone project
sudo mkdir -p $PROJECT_BASE_PATH
sudo git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH

# Create virtualenv
python3 -m venv $PROJECT_BASE_PATH/venv

# Install python packages
$PROJECT_BASE_PATH/venv/bin/pip install -r $PROJECT_BASE_PATH/requirements.txt
$PROJECT_BASE_PATH/venv/bin/pip install uwsgi==2.0.18

# Configure nginx
sudo cp $PROJECT_BASE_PATH/aws_terraform/deploy/nginx_profiles_api.conf /etc/nginx/sites-available/profiles_api.conf
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /etc/nginx/sites-available/profiles_api.conf /etc/nginx/sites-enabled/profiles_api.conf
sudo systemctl restart nginx

# Configure supervisor
sudo cp $PROJECT_BASE_PATH/aws_terraform/deploy/supervisor_profiles_api.conf /etc/supervisor/conf.d/profiles_api.conf
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl restart profiles_api
