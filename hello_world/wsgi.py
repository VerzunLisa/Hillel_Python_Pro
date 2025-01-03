import os
import sys

path = '/home/lika022/Hillel_Python_Pro/hello_world'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'hello_world.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
