import sys, os
INTERP = "/home/dwainebest/opt/python-3.6.2/bin/python3"
#INTERP is present twice so that the new python interpreter knows the actual executable path
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/SITENAME')  #You must add your project here

sys.path.insert(0,cwd+'/VIRTUALENV/bin')
#sys.path.insert(0,cwd+'/testGoat/lib/python3.6/site-packages/django')
sys.path.insert(0,cwd+'/testGoat/lib/python3.6/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "SITENAME.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
