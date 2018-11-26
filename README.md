# Regina

Regina is an AI that matches you up with victims of the same abuser while keeping your identity secret.

# Technologies

- Django
- Django Channels
- Websockets

# Getting it to work 

``` bash
easy_install virtualenv
```
``` bash
virtualenv -p python3.6 env && . env/bin/activate
```
If this command hangs it is almost certainly internet connectivity problems

``` bash
python --version && pip --version
```
This will output the version of python you are using. Make extra sure that both are using python3 by default.

``` bash
pip install -r requirements.txt
```
The psycopg2 module is sometimes finnicky so if it throws an error ping me and I'll come fix it.

``` bash
python manage.py makemigrations && python manage.py makemigrations submissions
```

``` bash
python manage.py migrate
```

``` bash
python manage.py runserver
```
