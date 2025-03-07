# settings/__init__.py
import os

# Default to dev settings for development
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.dev")
