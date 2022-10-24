
# Connecting Django with PostgreSQL database

Databases not configured (for safety reasons)!!!
Remember: don't keep sensitive data under Git's control! Such sensitive data are, inter alia, data to connect to the database. We keep this data in the local_settings.py file, which you will not find in this repository (the file is added to .gitignore)!

Have a look at the settings.py file, you will find the following section:

```python
try:
  from local_settings import DATABASES
except ModuleNotFoundError:
  print("Brak konfiguracji bazy danych w pliku local_settings.py!")
  print("Uzupełnij dane i spróbuj ponownie!")
  exit(0)
```

Add local_settings and fill with your data:

```python
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
```
