# CMPUT401MiniProject


virtualenv venv --python=python3
source venv/bin/activate
cd mysite
python manage.py makemigrations
python manage.py migrate
python manage.py runserver