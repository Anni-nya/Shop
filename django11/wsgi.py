"""
WSGI config for django11 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.insert(0, '/home/AnniPawsome/IdeaProjects/django11')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django11.settings')

application = get_wsgi_application()
