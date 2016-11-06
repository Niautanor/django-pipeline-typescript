from __future__ import unicode_literals

from django.conf import settings
from pipeline.compilers import SubProcessCompiler

DEFAULTS = {
    'TYPESCRIPT_BINARY': ('/usr/bin/env', 'tsc'),
    'TYPESCRIPT_ARGUMENTS': (None,)
}


class TypescriptCompiler(SubProcessCompiler):
    output_extension = 'js'

    def match_file(self, path):
        return path.endswith('.ts')

    def compile_file(self, infile, outfile, outdated=False, force=False):
        if not outdated and not force:
            return
        _settings = getattr(settings, 'PIPELINE', DEFAULTS)
        command = (
            getattr(_settings, 'TYPESCRIPT_BINARY',
                                DEFAULTS["TYPESCRIPT_BINARY"]),
            getattr(_settings, 'TYPESCRIPT_ARGUMENTS',
                               DEFAULTS["TYPESCRIPT_ARGUMENTS"]),
            infile,
            )
        return self.execute_command(command)
