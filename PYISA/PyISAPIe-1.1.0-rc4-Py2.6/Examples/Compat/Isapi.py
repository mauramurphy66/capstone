# $URL: https://pyisapie.svn.sourceforge.net/svnroot/pyisapie/Tags/1.1.0-rc4/PyISAPIe/Python/Examples/Compat/Isapi.py $
# $Rev: 91 $ $Date: 2008-01-10 23:53:59 -0800 (Thu, 10 Jan 2008) $
# (C)2008 Phillip Sitbon <phillip@sitbon.net>
#
"""Global ISAPI request handler.
"""
import imp

# The reason for using Env.SCRIPT_TRANSLATED instead of making
# it the interpreter map is so that Env can emulate the variable
# when using IIS 5.x.

if __interp__ != '__main__':
  __builtins__.__target__ = Env.SCRIPT_TRANSLATED
  Request = imp.load_source("__target__", __target__).Request

else:
  from Http import Config
  Config.InterpreterMap = "SCRIPT_NAME";
  Request = lambda: None
