Example Buildout Usage
======================

By default ``buildout.cfg`` extends on the latest stable version,
currently it is ``cellml-api-1.10.cfg``.  To use this, simply copy 
everything within this directory into your local disk, then::

    $ python bootstrap.py
    $ bin/buildout

This will take some time, but once the compiling is finished bootstrap 
should have generate a ``bin/cellmlpy`` which include the path to the
Python bindings.

Once this is done building, you can try to use this generated script 
with the example ``run.py`` as its parameter.
::

    $ bin/cellmlpy run.py
    loaded model: http://models.cellml.org/e/1/beeler_reuter_1977.cellml
    model cmetaid is: beeler_reuter_1977

It should also function as an interactive interpreter, however there was
a `bug`_ where the bootstrap constructor was causing exceptions that did
not get cleared correctly.  The exception would then be raised elsewhere
in the execution under certain circumstances, and in this case execution
of the interpreter is completely terminated (i.e. exit to shell).

This is no longer an issue in the latest development build, so if the
interactive shell is desired please feel free to modify ``buildout.cfg``
to extend the develment configuration file.

.. _bug: https://tracker.physiomeproject.org/show_bug.cgi?id=3054

File Details
============

``cellml-api-1.10.cfg``

  Builds the CellML API 1.10 with default option (everything enabled).

``cellml-api-1.11dev.cfg`` 

  Like the above, but builds the CellML API 1.11 development version.
  Since the URL and md5sum of the development tarball is not included,
  they are manually specified.  This version is included here solely
  because it contains a fix that clears expected exceptions raised
  during construction of bootstrap objects.
