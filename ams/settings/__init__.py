from settings._templates import TemplatesSettings
from settings._auth import AuthSettings
from settings._middleware import MiddlewareSettings
from settings._installed_apps import InstalledAppSettings
from settings._password_validators import PasswordValidatorSettings

__all__ = [
    "TemplatesSettings",
    "AuthSettings",
    "InstalledAppSettings",
    "PasswordValidatorSettings",
    "MiddlewareSettings",
]
