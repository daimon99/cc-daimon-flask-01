# coding: utf-8

from fabric.api import *

import sys

sys.path.append('.')


def dev():
    from {{cookiecutter.package_name}} import app
    app.run()
