"""
WSGI config for sato project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys

reload(sys)
sys.setdefaultencoding('utf-8')

import site

site.addsitedir('/var/www/env/lib/python2.7/site-packages')

# sys.path.append('/var/www/env/lib/python2.7/site-packages')
if not '/var/www/sato' in sys.path:
    sys.path.append('/var/www/sato')
if not '/var/www/sato/sato' in sys.path:
    sys.path.append('/var/www/sato/sato')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sato.settings")


activate_env = os.path.expanduser('/var/www/env/bin/activate_this.py')
execfile(activate_env, dict(__file__=activate_env))


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
