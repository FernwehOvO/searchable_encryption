"""
WSGI config for searchable_encryption project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# 设置WSGI的setting寻找路径
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'searchable_encryption.settings')

application = get_wsgi_application()



