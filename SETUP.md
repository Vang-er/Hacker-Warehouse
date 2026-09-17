python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

make your .env file!:
put in it those:

DB_NAME=hack_warehouse
DB_USER=hack_warehouse
DB_PASSWORD=hack_warehouse
DB_HOST=localhost
DB_PORT=8585

Then open SQL Shell (Psql)
CREATE DATABASE hack_warehouse;
CREATE USER hack_warehouse WITH PASSWORD 'their_own_password';
GRANT ALL PRIVILEGES ON DATABASE hack_warehouse TO hack_warehouse;

(Everything Should match the .env!!!)

then migrate by using : python manage.py migrate
then create ur superuser by: python manage.py createsuperuser
