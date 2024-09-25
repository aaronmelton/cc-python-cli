# !/usr/bin/env python
# -*- coding: utf-8 -*-
#

import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def print_instructions():
    print("")
    print("Run these commands to complete project creation:")
    print("1. cd {{ cookiecutter.project_name }}")
    print("2. poetry shell")
    print("3. poetry update")
    print("")

if __name__ == '__main__':
    if "{{ cookiecutter.generate_docker_files }}" == "no":
        for filename in [".dockerignore", "docker-compose.yml", "docker_build.sh", "Dockerfile", "entrypoint.sh"]:
            remove_file(filename)
    print_instructions()