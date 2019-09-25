"""
WSGI config for ClassroomProduct project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ClassroomProduct.settings')
#
# application = get_wsgi_application()

import os
import sys

path='/home/beckss/PycharmProjects/ClassroomProduct'

if path not in sys.path:
  sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'ClassroomProduct.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
