Overview
========

This is the recipe that will build the CellML API Python bindings with
all options enabled by default.  Currently, there are some limitations,
such as all dependencies must be installed manually, and I don't think
this will work under Windows at the moment.


Supported options
=================

The recipe supports the following options:

api-version
    CellML API version to build.  Valid versions any versions that build
    via CMake and has Python bindings (>1.10), and must be present in
    the list of valid versions.

cmake-generator
    The generator to use.  Only `Unix Makefiles` is supported

check-build
    Whether to check build time dependencies.  Default is off because it
    didn't detect GSL libraries even though it was installed for me.
    Same as passing `-DCHECK_BUILD:BOOL=OFF` to `cmake`.

Other supported options:

    - enable-examples
    - enable-annotools
    - enable-ccgs
    - enable-celeds
    - enable-celeds-exporter
    - enable-cevas
    - enable-cis
    - enable-cuses
    - enable-gsl-integrators
    - enable-malaes
    - enable-python
    - enable-rdf
    - enable-spros
    - enable-srus
    - enable-telecems
    - enable-vacss

Please refer to the CellML API Documentations for what these options do.


Example usage
=============

.. Note to recipe author!
   ----------------------
   zc.buildout provides a nice testing environment which makes it
   relatively easy to write doctests that both demonstrate the use of
   the recipe and test it.
   You can find examples of recipe doctests from the PyPI, e.g.
   
     http://pypi.python.org/pypi/zc.recipe.egg

   The PyPI page for zc.buildout contains documentation about the test
   environment.

     http://pypi.python.org/pypi/zc.buildout#testing-support

   Below is a skeleton doctest that you can start with when building
   your own tests.

We'll start by creating a buildout that uses the recipe::

    >>> write('buildout.cfg',
    ... """
    ... [buildout]
    ... parts = test1
    ...
    ... [test1]
    ... recipe = cellml.recipe.api
    ... option1 = %(foo)s
    ... option2 = %(bar)s
    ... """ % { 'foo' : 'value1', 'bar' : 'value2'})

Running the buildout gives us::

    >>> print 'start', system(buildout) # doctest:+ELLIPSIS
    start...
    Installing test1.
    Unused options for test1: 'option2' 'option1'.
    <BLANKLINE>


