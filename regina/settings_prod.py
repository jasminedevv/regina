"""
Settings unique to a production environment

Using MySQL on Passenger

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
# do it like this because sometimes passenger crashes and reveals your environment variables

DEBUG = False

ALLOWED_HOSTS = ['regina-app.herokuapp.com']

# DATABASES = db_options

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

# this will probably be /public or something so that it can get static files at /public/static
# STATIC_ROOT = 'some/path/idk'