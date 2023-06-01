# REITs Rentals

python and django

(https://www.youtube.com/watch?v=nWBgg2QXtSA)

apt-get install python3-venv

python3 -m venv virtual

source ./virtual/bin/activate

source ./virtual/bin/deactivate


pip freeze

pip install django

django-admin startproject dentist
django-admin.py startproject dentist
python3 django-admin.py startproject dentist

#run server (https://dockerize.io/guides/python-django-guide)
python manage.py runserver

python manage.py migrate

python manage.py makemigrations

admin: 
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site

python3 manage.py createsuperuser

edit
in /home/ibrahim/sandbox/anasse/dentist/dentist/settings.py
ALLOWED_HOSTS = ["*"]

and
/home/ibrahim/sandbox/anasse/virtual/lib/python3.9/site-packages/django/conf/global_settings.py

and 
/home/ibrahim/sandbox/anasse/virtual/lib/python3.9/site-packages/django/core/management/commands/runserver.py
default_port = "8090"

python manage.py startapp website

edit
/home/ibrahim/sandbox/anasse/dentist/dentist/settings.py
add under INSTALLED_APPS = [
 "website", 
 
 Python Django Dentist Website #4
(https://www.youtube.com/watch?v=cUaZ0ElJ760)



# start local smtp server - atviavate virtual env first
python -m smtpd -n -c DebuggingServer localhost:1025

See:
django enviromental passsword

python dictionaries

#hosting online

pip install gunicorn
pip install django-heroku
pip install dj_database_url
pip install python-decouple
touch Procfile
pip freeze
pip freeze > requirements.txt