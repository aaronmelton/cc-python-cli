#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    """Remove a file if it exists."""
    try:
        file_path = os.path.join(PROJECT_DIRECTORY, filepath)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Removed: {filepath}")
    except OSError as e:
        print(f"Warning: Could not remove {filepath}: {e}")

def print_instructions():
    print("")
    print("Run these commands to complete project creation:")
    print("1. cd {{ cookiecutter.project_directory }}")
    print("2. eval $(poetry env activate)")
    print("3. poetry update")
    print("")

if __name__ == '__main__':
    if "{{ cookiecutter.generate_docker_files }}" == "no":
        for filename in [".dockerignore", "docker-compose.yml", "docker_build.sh", "Dockerfile", "entrypoint.sh"]:
            remove_file(filename)
    print_instructions()