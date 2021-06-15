# custom django settings for Chiron RDCRN django site

from .settings_global import *

ALLOWED_HOSTS = ['*']
SECRET_KEY = '44JVnJCjrfsrqYfXgGsDdFsCMcECBRKm5nC5srTkWT8cTTJw22nUAhA6cP67'

WSGI_APPLICATION = 'project.wsgi_docker.application'

# want to just use public schema for docker postgres, otherwise you'll get permission errors
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'rdcrn',
        'USER': 'rdcrn_app',
        'PASSWORD': 'G2J8EfJgUQ8SCJar',
        'HOST': 'postgres',
        'PORT': 5432,
    }
}

# No router because only 1 schema
# DATABASE_ROUTERS = ['project.router.CustomDatabaseRouter']

CHI_AUTH_API_ACCESS_TOKEN = 'get_access_token'
CHI_AUTH_URL = 'https://chi-dev.uc.edu/auth/'



STATIC_ROOT = '/static/'		# this needs to match with docker compose static volume
STATIC_URL = '/static/'

CHIRON_MONGO_CONNECTION_SETTINGS = {
    'host' : 'mongo',
}