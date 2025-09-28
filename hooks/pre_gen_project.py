#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Borrowed from https://github.com/tedivm/robs_awesome_python_template/blob/main/hooks/pre_gen_project.py

import sys
from re import match as re_match


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
module_name = '{{ cookiecutter.project_slug }}'
python_version = '{{ cookiecutter.python_version }}'

# Validate module name
if not re_match(MODULE_REGEX, module_name):
    print('ERROR: The project slug (%s) is not a valid Python module name. Please do not use a - and use _ instead' % module_name)
    sys.exit(1)

# Validate Python version
try:
    major, minor = map(int, python_version.split('.')[:2])
    if major != 3 or minor < 12:
        print('ERROR: Python version must be 3.12 or higher. Got: %s' % python_version)
        sys.exit(1)
except ValueError:
    print('ERROR: Invalid Python version format: %s' % python_version)
    sys.exit(1)