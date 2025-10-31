This example provides backwards compatibility with version 1.0.0.
There is one minor difference - __target__ will be prepended
with '\\?\' to represent a string that is able to be longer than
MAX_PATH - this was cut out in 1.0.0. You can remove this difference
by cutting it out within the initialization of the main request
handler.

To use, put Isapi.py in The Http package.