create virtual environment using command " python3 -m venv env "
activate virtual environment by command "source env/bin/activate"
the run following commands below
pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata superuser_data.json