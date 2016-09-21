"""
WSGI config for joshua_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

##following code is used for development in Ubuntu14.04 Apache2##
import sys
sys.path.append("/home/joshua/CODE/PYTHON/joshua_blog/")
#################################################################

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "joshua_blog.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
