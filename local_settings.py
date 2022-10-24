# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '* database name *',
        'HOST': 'localhost',
        'PASSWORD': '* password *',
        'USER': '*your username*',
        'PORT': 5432,
    }
}