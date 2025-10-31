# $URL: https://pyisapie.svn.sourceforge.net/svnroot/pyisapie/Tags/1.1.0-rc4/PyISAPIe/Python/Examples/Regex/Isapi.py $
# $Rev: 91 $ $Date: 2008-01-10 23:53:59 -0800 (Thu, 10 Jan 2008) $
# (C)2008 Phillip Sitbon <phillip@sitbon.net>
#
"""Global ISAPI request handler.
"""
from Http import *
import re

MapURL = { \
  r'^/blog/{0,1}$':
    'WWW.Blog.Main.Request',
  r'^/blog/read$':
    'WWW.Blog.Read.Request',
  r'^/blog/archive/(\d{4})/(\d{2})/(\d{2})(?:/(?P<Entry>\d{2})){0,1}$':
    'WWW.Blog.Archive.Request',
}

FastMaps = []
Cache = {}

for Pattern, Handler in MapURL.items():
  Re = re.compile(Pattern)
  Module, Function = Handler.rsplit('.', 1)
  Handler = getattr(__import__(Module,(),(),('',)), Function)
  FastMaps.append((Re.match, Handler))

FastMaps = tuple(FastMaps)

def Request():
  URL = Env.URL

  if URL in Cache:
    I = Cache[URL]
    return I[0](*I[1],**I[2])

  for Match, Handler in FastMaps:
    R = Match(URL)
    if R:
      Cache[URL] = (Handler, R.groups(), R.groupdict())
      return Handler(* R.groups(), ** R.groupdict())

  Header(Status = 404, Close = True)
  print "Not Found"
  

