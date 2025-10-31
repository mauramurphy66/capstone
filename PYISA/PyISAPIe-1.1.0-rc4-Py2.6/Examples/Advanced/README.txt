This example includes a more comprehensive form of
URL-to-handler mapping along with a mechanism that
allows modules to be reloaded when they are changed
if the Debug config parameter is set.

How to use:

 Put the three .py files in this folder inside the
Http package (Isapi.py, URL.py, and Watch.py). Put
the WWW package folder somewhere in your import
path. For this setup, I like to have the web stuff
separate, so I use the system environment variable
PYTHONPATH to specify a special folder such as
D:\Web\Lib to hold the Http and WWW packages. It
would be best to make sure that wherever they end up,
they aren't in any web site's folder.

Edit WWW/URL.py to match the hadlers you would like
to use. To use this example out of the box, make a
virtual directory named /dev with PyISAPIe as the
wildcard application map, and make sure to uncheck
"Verify that file exists".

Edit the Config.Debug parameter to enable or disable
reloading of handler modules.