#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Gregory Oschwald
# Copyright (c) 2014 Gregory Oschwald
#
# License: MIT
#

"""This module exports the Rustc plugin class."""

from SublimeLinter.lint import Linter
import os


class Rust(Linter):

    """Provides an interface to Rust."""

    workdir = os.getcwd()
    while True:
        if "Cargo.toml" in os.listdir(workdir):
            break
        elif workdir == '/':
            workdir = os.getcwd()
            break
        else:
            workdir = os.path.split(workdir)[0]
            continue

    syntax = 'rust'
    cmd = 'rustc --no-trans -L%s -L%s' % (workdir + '/target', workdir + '/target/deps')
    tempfile_suffix = 'rs'

    regex = (
        r'^.+?:(?P<line>\d+):(?P<col>\d+):\s+\d+:\d+\s'
        r'(?:(?P<error>(error|fatal error))|(?P<warning>warning)):\s+'
        r'(?P<message>.+)'
    )
