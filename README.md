# Architecture

A Django based  Web framework，integrated with user login, registration, distributed role based permission management and  front-end UI

# Deploy:
1.Install packages:
`pip install -r requirements.txt`

2.Create database
Edit database configuration in settings.py, then use your local mysql, source architecture_20151231.sql

3.Run
`python manage.py runserver 0.0.0.0:8000`
You may need to `python manage.py makemigrations` if cann't start normaly.
