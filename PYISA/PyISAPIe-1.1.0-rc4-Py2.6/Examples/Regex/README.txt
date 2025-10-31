This demonstrates using regular expressions to do
URL matching and in turn run an appropriate request
handler. This is a preferred method of creating sites,
since it provides maximum flexibility. The average
measured overhead, thanks to the URL caching, is about
15-20 microsenconds.

I have to give credit to Django for inspiring this
method of request handling.

To use, put Isapi.py in the Http package.

If you want the ISAPI handler to recieve requests for
arbitrary URLs, you can either make the wildcard
application map for your entire site (rather than adding
an associated extension), or you can create a virtual
directory, i.e. /stuff, that has a wildcard map. The
latter is good if you want to isolate teh behavior,
because you will only be processing URLs that begin with
/stuff. Feel free to write if you have questions!