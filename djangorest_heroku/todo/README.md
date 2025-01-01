# Steps to build

```bash
cd <root>/todo
python -m venv .venv 
source .venv/Scripts/activate
python -m pip install django~=4.0.0
python -m pip install djangorestframework~=3.13.0
python -m pip install django-cors-headers~=3.10.0

django-admin startproject django_project .
python manage.py migrate

python manage.py startapp todos
python manage.py makemigrations todos
python manage.py migrate
python manage.py test todos

python manage.py createsuperuser

python manage.py runserver
```

# Prepare Heroku deployment

```bash
mkdir static
cd static
python -m pip install whitenoise==5.3.0 # tool that helps to serve static files
python manage.py collectstatic
python -m pip install gunicorn~=20.1.0 # will be used as production web server for the application
python -m pip freeze > requirements.txt
mkdir runtime.txt # insert python version to be used
mkdir Procfile # insert start command for the app
```

# Deploy to Heroku

```bash
cd <root>
heroku login
heroku git:remote -a python-django-todos # heroku app will point to git repo
heroku create python-django-todos # heroku creates a container for the app, name must be globally unique

git subtree split --prefix library main --branch temp_todos # create temp branch from todos subfolder
git push heroku temp_todos:main --force # deploy content from temp_todos branch to heroku

heroku ps:scale web=1 # deploy on one container 
heroku open # open app url

heroku logs --tail # check logs for deployment
heroku ps:scale web=0 # remove deployment
```