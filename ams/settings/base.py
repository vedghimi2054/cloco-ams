import os

from configurations import Configuration
from configurations.values import DatabaseURLValue
from dotenv import load_dotenv

from settings._auth import AuthSettings
from settings._installed_apps import InstalledAppSettings
from settings._middleware import MiddlewareSettings
from settings._password_validators import PasswordValidatorSettings
from settings._templates import TemplatesSettings

load_dotenv()


class BaseSettings(Configuration):
    # Load the SECRET_KEY from the environment variable
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')  # Provide a fallback if not set

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = os.getenv('DEBUG', 'True') == 'True'

    # ALLOWED_HOSTS: You can specify multiple allowed hosts separated by commas
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

    INSTALLED_APPS = InstalledAppSettings.INSTALLED_APPS

    MIDDLEWARE = MiddlewareSettings.MIDDLEWARE

    REST_FRAMEWORK = AuthSettings.REST_FRAMEWORK
    AUTH_USER_MODEL = AuthSettings.AUTH_USER_MODEL
    SIMPLE_JWT = AuthSettings.SIMPLE_JWT

    ROOT_URLCONF = 'core.urls'
    # database is overloaded
    DATABASES = DatabaseURLValue()

    TEMPLATES = TemplatesSettings.TEMPLATES

    WSGI_APPLICATION = 'core.wsgi.application'

    # Password validation
    # https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
    AUTH_PASSWORD_VALIDATORS = PasswordValidatorSettings.AUTH_PASSWORD_VALIDATORS

    # Internationalization
    # https://docs.djangoproject.com/en/5.1/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/5.1/howto/static-files/

    STATIC_URL = 'static/'

    # Default primary key field type
    # https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
