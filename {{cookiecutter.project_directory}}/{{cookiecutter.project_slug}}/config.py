"""{{ cookiecutter.project_name }} Config Class."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
#


from dataclasses import dataclass
from datetime import datetime
from os import environ as os_environ


@dataclass
class Config:
    """Class for Application variables."""

    def __init__(self):
        """Application Variables."""
        self.app_dict = {
            "author": "{{ cookiecutter.author }}",
            "date": "{{ cookiecutter.project_date }}",
            "desc": "{{ cookiecutter.project_description }}",
            "title": "{{ cookiecutter.project_slug }}",
            "url": "{{ cookiecutter.project_url }}",
            "version": "{{ cookiecutter.version }}",
        }

        # Logging Variables
        self.log_dict = {
            "filename": f"""{os_environ.get("LOG_PATH", "./log/")}{self.app_dict["title"]}_{datetime.now().strftime("%Y%m%d")}.log""",
            "level": os_environ.get("LOG_LEVEL", "INFO"),
            "path": os_environ.get("LOG_PATH", "./log/"),
        }

        # API Keys
        self.key_dict = {
            "api_key": os_environ.get("API_KEY", None),
        }
