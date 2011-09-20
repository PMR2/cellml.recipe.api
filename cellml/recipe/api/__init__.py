# -*- coding: utf-8 -*-
"""Recipe api"""

import zc.recipe.cmmi


class Recipe(zc.recipe.cmmi.Recipe):
    """\
    CellML API building recipe.

    Currently it's a direct clone of zc.recipe.cmmi, until specific
    modifications are required.

    There are new options introduced, and they are:

      - api-version
      
        Version number of the CellML API.  Valid versions any versions
        that build via CMake and has Python bindings (>1.10), and must
        be present in the list of valid versions.

      - cmake-generator

        The generator to use.  Only `Unix Makefiles` is supported

      - check-build

        Whether to check build time dependencies.  Default is off 
        because it didn't detect GSL libraries even though it was
        installed for me.

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

        Please refer to the CellML API Documentations for what these
        options do.

    """

    option_passthru_keys = [
        'autogen',  # XXX to be ignored because autogen is not used.
        'patch',
        'patch_options',
        'environment',
        'configure-options',  # this gets processed first
    ]

    option_cmake_map = {
        'check-build': 'off',
        'enable-examples': 'on',
        'enable-annotools': 'on',
        'enable-ccgs': 'on',
        'enable-celeds': 'on',
        'enable-celeds-exporter': 'on',
        'enable-cevas': 'on',
        'enable-cis': 'on',
        'enable-cuses': 'on',
        'enable-gsl-integrators': 'on',
        'enable-malaes': 'on',
        'enable-python': 'on',
        'enable-rdf': 'on',
        'enable-spros': 'on',
        'enable-srus': 'on',
        'enable-telecems': 'on',
        'enable-vacss': 'on',
    }

    def __init__(self, buildout, name, options):
        self.original_options = options

        # build a set of modified options customized for this.
        api_options = {}
        self.api_version = options.get('api-version', None)
        self.cmake_generator = options.get('cmake-generator', 'Unix Makefiles')

        api_options['url'], api_options['md5sum'] = get_api_info(
            self.api_version)
        api_options['source-directory-contains'] = options.get(
            'source-directory-contains', 'CMakeLists.txt')
        api_options['configure-command'] = options.get(
            'configure-command', 'cmake')

        # construct extra options
        extra_options = self.build_options(self.cmake_generator, options)
        api_options['extra_options'] = extra_options

        # continue on with the parent, with our modified options.
        super(Recipe, self).__init__(buildout, name, api_options)

        # further processing

    def build_options(self, cmake_generator, options):
        results = []
        results.append("-G '%s'" % cmake_generator)
        for k, v in self.option_cmake_map.iteritems():
            # convert to cmake keys.
            confkey = k.replace('-', '_').upper()
            results.append('-D%s:BOOL=%s' % (confkey, options.get(k, v)))

        # construct the `extra_options` string
        return ' '.join(results)

    def cmmi(self, dest):
        if self.configure_options is None:
            # unless it got assigned earlier
            self.configure_options = \
                '-DCMAKE_INSTALL_PREFIX:PATH=%s ' \
                '-DCMAKE_INSTALL_RPATH:PATH=%s/lib' % (dest, dest)

        return super(Recipe, self).cmmi(dest)

def get_api_info(version):
    # XXX update this method to acquire matching url/md5sum of specified
    # version from a list of valid combinations for the API.

    url = 'http://sourceforge.net/projects/cellml-api/files/CellML-API-Nightly/1.10/20110913/src/cellml-api-1.10.tar.bz2/download'
    md5sum = '37a2cf957e9db43e21c9e43f6ec3b17f'

    return url, md5sum
