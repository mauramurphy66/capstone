# $URL: https://pyisapie.svn.sourceforge.net/svnroot/pyisapie/Tags/1.1.0-rc4/PyISAPIe/Python/Http/Isapi.py $
# $Rev: 165 $ $Date: 2009-06-15 14:19:18 -0700 (Mon, 15 Jun 2009) $
# (C)2008 Phillip Sitbon <phillip@sitbon.net>
#
"""Global ISAPI request handler.

All requests go here - after the first successful
import of this module & Request() function, it
will not be reloaded for the life of the interpreter.

This default simply attempts to load the file targeted
by the URL and call its Request() function. Although
SCRIPT_TRANSLATED is not available in IIS 5.x, it is
emulated for completeness.

I don't really recommend this method - it's not as
package/module oriented as the Regex and Advanced
examples, which can handle arbitrary URLs and pass
them to preloaded handlers.

ALSO: imp.load_source is NOT case-sensitive and doesn't
follow the typical import case rules. You might like this
but it's really not great behavior.

See example Isapi.py files in ../Examples, including
one that makes this version backwards compatible with
v1.0.0 (in the Compat folder).
"""
from PyISAPIe import Env
from hashlib import md5
import imp

Handlers = {}


def Request():
  Script = Env.SCRIPT_NAME
  Key = Name = '__'+md5(Script).hexdigest().upper()
  Handler = Handlers.get(Key, None)

  if not Handler:
    try:
      Handlers[Key] = imp.load_source(Key, Env.SCRIPT_TRANSLATED).Request
    except Exception, Val:
      # trigger a passthrough to the next ISAPI handler -
      # ONLY WORKS FOR WILDCARD APPLICATION MAPPINGS
      return True
      # or just fail, preferable for an application map
      #raise ImportError, "[Loading '%s'] %s" % (Env.SCRIPT_TRANSLATED, str(Val))


  return Handlers[Key]()
