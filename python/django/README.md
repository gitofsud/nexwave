# Steps to use Django Framework:

1. Create Project

        django-admin startproject project_name

2. Run Server

        python manage.py runserver

3. Create admin credentials

        python manage.py createsuperuser

4. Create Schema (make migrations) and execute schema on DB (migrate)

        python manage.py makemigrations  
        python manage.py migrate  

5. Create app

        python manage.py startapp home
    
    - settings.py -> Installed Apps -> Add 'home'