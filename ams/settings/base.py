import os

from configurations import Configuration
from configurations.values import DatabaseURLValue
from dotenv import load_dotenv

from settings import AuthSettings, InstalledAppSettings, MiddlewareSettings, PasswordValidatorSettings, \
    TemplatesSettings

load_dotenv()


class BaseSettings(Configuration):
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    DEBUG = os.getenv('DEBUG', 'True') == 'True'
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

    INSTALLED_APPS = InstalledAppSettings.INSTALLED_APPS

    MIDDLEWARE = MiddlewareSettings.MIDDLEWARE

    REST_FRAMEWORK = AuthSettings.REST_FRAMEWORK
    AUTH_USER_MODEL = AuthSettings.AUTH_USER_MODEL
    SIMPLE_JWT = AuthSettings.SIMPLE_JWT

    ROOT_URLCONF = 'core.urls'

    DATABASES = DatabaseURLValue()

    TEMPLATES = TemplatesSettings.TEMPLATES

    WSGI_APPLICATION = 'core.wsgi.application'
    AUTH_PASSWORD_VALIDATORS = PasswordValidatorSettings.AUTH_PASSWORD_VALIDATORS

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_TZ = True

    STATIC_URL = 'static/'

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
