Starting Django project

python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject project .
python manage.py startapp contact


Setting git

git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main

Setting .gitignore

git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT


Migrating Django database

python manage.py makemigrations
python manage.py migrate


Creating and modifying password of a Django super user

python manage.py createsuperuser
python manage.py changepassword USERNAME