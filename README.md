# Django rest API application 

# About Project

Small example of Django REST API for departments and employees with token security authentication.

Organization have some departments and employees, which are belong to one of them. 
Departments and employees can be added/edited/removed or showed with or without pagination using API

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

# Command were used during the project creation process
- django-admin startproject python_django_department
- python manage.py startapp departments_api
- python manage.py startapp departments_api_v2

# Command were used on a first startup to init database
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser

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
