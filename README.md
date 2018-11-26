# Regina

Regina is an AI that matches you up with victims of the same abuser while keeping your identity secret.

# Technologies

- Django
- Django Channels
- Websockets

# Getting it to work 

```easy_install virtualenv```
```virtualenv -p python3.6 env && . env/bin/activate``
If this command hangs it is almost certainly internet connectivity problems

```python --version && pip --version```
This will output the version of python you are using. Make extra sure that both are using python3 by default.

```pip install -r requirements.txt```
The psycopg2 module is sometimes finnicky so if it throws an error ping me and I'll come fix it.

```python manage.py makemigrations && python manage.py makemigrations submissions```

```python manage.py migrate```

```python manage.py runserver```