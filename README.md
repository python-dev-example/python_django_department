# Django rest API application 

# About Project

Small example of Django REST API for departments and employees with token security authentication.


# Used libraries

- Django
- Django money
- Django filter
- Django REST framework
- Django REST framework JWT
- Django REST framework jsonapi
- Djoser
- MySQL client

To freeze library versions python command can be used:

```
pip freeze -> requirements.txt
```

# Was done during the project creation process
django-admin startproject python_django_department
python manage.py startapp departments_api

# Needs to be user on first start to init database
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# Start application

To start application from terminal command below can be used:
```
python manage.py runserver
```

# To check migration sql query use:
```
python manage.py sqlmirgate {app_name_here} {migration_number_here}
```

for example:
```
python manage.py sqlmigrate departments_api 0001
```
