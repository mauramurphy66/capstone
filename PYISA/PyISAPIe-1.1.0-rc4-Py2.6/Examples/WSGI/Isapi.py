# $URL: https://pyisapie.svn.sourceforge.net/svnroot/pyisapie/Tags/1.1.0-rc4/PyISAPIe/Python/Examples/WSGI/Isapi.py $
# $Rev: 95 $ $Date: 2008-01-11 11:07:35 -0800 (Fri, 11 Jan 2008) $
# (C)2008 Phillip Sitbon <phillip@sitbon.net>
#
"""Global ISAPI request handler for use with WSGI applications.

This example merges two WSGI applications and also runs scripts
directly.

If you don't have either Django or Trac, comment out that section
and the entry in "Apps" and it should work fine.

You may also believe that you can run multiple Django projects just
by choosing the DJANGO_SETTINGS_MODULE environment variable based
on the URL, but beware- that is a process-level value you're
changing! I'm not sure if the value is also looked for in the WSGI
environment. For now, I'm just leaving it at one project.

I chose to place the root folder under /app for the specific
purpose of making PyISAPIe the wildcard handler for that path only.
For IIS 5.x, all the paths must end in ".py" because an extension
must be associated with a handler.

See the install docs for further information, and the WSGI setup
page for specifics about getting this script going.
"""
from Http.WSGI import RunWSGI
from Http import Env
from md5 import md5
import imp
import os

#
# Django rev 7002
#
# Due to the nature of this particular script, all the urls in
# Django must start with /app/django/, or whatever you specify
# below.
#
from django.core.handlers.wsgi import WSGIHandler as DjangoHandler
os.environ["DJANGO_SETTINGS_MODULE"] = "myapp.settings"

#
# Trac 0.10.4 (worked, but could not fully verify)
#
# Aside from other issues, I wasn't patient enough to figure
# out how to specify a base URL for Trac. In general, it
# appeared to work.
#
from trac.web.main import dispatch_request as TracHandler
os.environ["TRAC_ENV_PARENT_DIR"] = r"C:\Path\To\Trac" # or TRAC_ENV

#
# Simple script handling.
#
# Just a copy of what's in the Request() of the default handler.
#
# If of course assumes that the file specified by the URL
# is valid.
#
ScriptHandlers = {}
def RunScript(Path):
  global ScriptHandlers
  try:
    # attempt to call an already-loaded request function.
    return ScriptHandlers[Path]()
  except KeyError:
    # uses the script path's md5 hash to ensure a unique
    # name - not the best way to do it, but it keeps
    # undesired characters out of the name that will
    # mess up the loading.
    Name = '__'+md5(Path).hexdigest().upper()
    ScriptHandlers[Path] = \
      imp.load_source(Name, Env.SCRIPT_TRANSLATED).Request
    return ScriptHandlers[Path]()

#
# URL prefixes to map to the roots of each application.
#
Apps = {
  "/app/django/"  : lambda P: RunWSGI(DjangoHandler()),
  "/app/trac/"    : lambda P: RunWSGI(TracHandler),
  "/app/scripts/" : lambda P: RunScript(P),
}

#
# The main request handler.
#
def Request():
  # Might be better to do some caching here?
  Name = Env.SCRIPT_NAME

  # Apps might be better off as a tuple-of-tuples,
  # but for the sake of representation I leave it
  # as a dict.
  for App, Handler in Apps.items():
    if Name.startswith(App):
      return Handler(Name)

  # Cause 500 error: there should be a 404 handler, eh?
  #
  raise Exception, "Handler not found."
