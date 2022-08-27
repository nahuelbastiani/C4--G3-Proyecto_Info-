from .base import *


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Grupal',
        'USER': 'postgres',
        'PASSWORD': '6yoHPsCkgL9Z6DCRcmhq',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Nahuel Local
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'ong',
#         'USER': 'postgres',
#         'PASSWORD': '1234',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }