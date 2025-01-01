# Steps to build

```bash
cd <root>/blogapi
python -m venv .venv 
source .venv/Scripts/activate
python -m pip install django~=4.0.0
python -m pip install djangorestframework~=3.13.0
python -m pip install django-cors-headers~=3.10.0

django-admin startproject django_project .

python manage.py startapp accounts
python manage.py makemigrations accounts
python manage.py migrate

python manage.py startapp posts
python manage.py makemigrations posts
python manage.py migrate
python manage.py test posts

python manage.py createsuperuser

python manage.py runserver
```

# Prepare Heroku deployment

```bash
mkdir static
cd static
python -m pip install whitenoise==5.3.0 # tool that helps to serve static files
python manage.py collectstatic
python -m pip install psycopg2==2.9.3 # database adapter between django app and PostgreSQL, needs db installed when the os
python -m pip install gunicorn==20.1.0 # will be used as production web server for the application
python -m pip freeze > requirements.txt
mkdir runtime.txt # insert python version to be used
mkdir Procfile # insert start command for the app
```

# Deploy to Heroku

```bash
cd <root>
heroku login
heroku git:remote -a python-django-blogapi # heroku app will point to git repo
heroku create python-django-blogapi # heroku creates a container for the app, name must be globally unique

heroku addons:create heroku-postgresql:mini # creates a PostgreSQL db on heroku
heroku config:set SECRET_KEY="DJANGO_SECRET_KEY" # add env var to heroku, other 2 env var are already defined DATABASE_URL (when creating db in heroku) and DEBUG has False value as default
heroku config # check env vars in heroku

git subtree split --prefix blogapi main --branch temp_blogapi # create temp branch from blogapi subfolder
git push heroku temp_blogapi:main --force # deploy content from temp_blogapi branch to heroku
heroku ps:scale web=1 # deploy on one container 

heroku run python manage.py migrate # provision the new PostgreSQL db
heroku run python manage.py createsuperuser

heroku open # open app url

heroku ps:scale web=0 # remove deployment
heroku logs --tail # check logs for deployment
```

# Implement authentication and registration

```bash
python -m pip install dj-rest-auth==2.1.11 # for login logout purposes
python -m pip install django-allauth~=0.48.0 # for registration
```

# Document project

```bash
python -m pip install drf-spectacular~=0.21.0
python manage.py spectacular --file schema.yml

```
 # Environment variables

```bash
 python -m pip install 'environs[django]==9.5.0'
 python -c "import secrets; print(secrets.token_urlsafe())" # generate a new Django SECRET_KEY

 ```