from .base import *


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres2',
        'USER': 'postgres',
        'PASSWORD': 'Proyectopgs2022!',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
