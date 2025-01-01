# Create vagrant development server

```bash
vagrant init ubuntu/bionic64
vagrant up
vagrant ssh
```

# Create django project on vagrant server

```bash
cd /vagrant
python -m venv ~/venv
source ~/venv/bin/activate
pip install -r requirments.txt

django-admin.py startproject django_project . 
python manage.py startapp profiles_api
```

# Run django project

```bash
python manage.py runserver 0.0.0.0:8000
```

# Generate and run migration on db

```bash
python manage.py makemigrations profiles_api
python manage.py migrate
```

# Create django superuser

```bash
python manage.py createsuperuser


# superuser account /admin login data:
# admin@admin.com/admin

# /api/login endpoint
# used for login

# /api/profiles endpoints
# GET verbes allowed for all users without login
# logged in users can make modifications on their own profile

# /api/feeds endpoints:
# logged in user can only see and make modifications on their own feed

```