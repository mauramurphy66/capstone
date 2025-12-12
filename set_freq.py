
from xmlrpc.client import ServerProxy
s = ServerProxy('http://localhost:8081')
s.set_NOAA_gain(0)
