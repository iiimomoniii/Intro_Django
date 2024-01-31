### Intro_Django

Python Version 3.9.18
Django Version (4, 2, 9, 'final', 0)

### django overview (MVT Model View Template)
request ->  Chrome  => URL (urls.py) => View (views.py) => Template (*.html)
response -> Template (*.html) => View (views.py) => Chrome

### 0
#install python
#install pip 

pip install django

### 1 create project
django-admin startproject <project-name>
django-admin startproject myproject

### 2 start project
cd ../BasicTutorial/myproject
python manage.py runserver

### 3 view
http://127.0.0.1:8000


### 4 create AppLevel
python manage.py startapp <app-name>
python manage.py startapp myapp

### 5 register app to project

### 6 import urls of AppLevel

### 7 create model
python manage.py makemigrations
python manage.py migrate
