# Django Rest Framework Learning Project

```bash
This is a Django project with multiple basic apps designed to help in learning the Django Rest  
Framework. The project covers various aspects of the framework, including ViewSets, Models, Serializers,  
and adding Permissions and Authorizations to users.
```

# Steps to build project

```bash
django-admin startproject DjangoRestApp .
python manage.py migrate

python manage.py createsuperuser

python manage.py startapp PeopleApp
python manage.py makemigrations PeopleApp
python manage.py migrate

python manage.py startapp ArtifactsApp
python manage.py makemigrations ArtifactsApp
python manage.py migrate

python manage.py startapp BooksApp
python manage.py makemigrations BooksApp
python manage.py migrate

python manage.py startapp VehiclesApp
python manage.py makemigrations VehiclesApp
python manage.py migrate

python manage.py startapp SinglePageApp

python manage.py runserver 127.0.0.1:80

curl -s http://127.0.0.1:80/api/artifacts/ | python -m json.tool
curl -s -X POST -d "name=post_new_item" -d "shiny=True" http://127.0.0.1:80/api/artifacts/

```