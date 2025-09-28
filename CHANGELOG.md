# CHANGELOG


## [0.2.0] - 2025-09-28
### Added
- .github/workflows/ci.yml: Complete GitHub Actions CI pipeline with multi-Python version testing, linting, and code coverage.
- .pre-commit-config.yaml: Pre-commit hooks configuration for automated code quality checks.
- pyproject.toml: Added mypy, pre-commit dependencies and mypy configuration section.
### Changed
- cookiecutter.json: Added sensible default values, dynamic date generation, Python version selection limited to supported versions (3.12+), and improved project URL generation.
- hooks/pre_gen_project.py: Added Python version validation (3.12+), fixed shebang formatting.
- hooks/post_gen_project.py: Added error handling for file removal, fixed project directory reference, improved logging.
- pyproject.toml: Modernized Python version specification to ">=3.12,<4.0", updated all dependencies to latest versions, updated mypy target version to 3.12.
- .gitignore: Enhanced with additional IDE files, OS-specific files, and project-specific ignores.
- {{cookiecutter.project_slug}}.py: Fixed import order (local imports after third-party), added comprehensive type hints and typing imports.
- .github/workflows/ci.yml: Updated GitHub Actions workflow to escape template expressions and only test supported Python versions (3.12, 3.13).
### Removed
- cookiecutter.json: Removed unsupported Python versions (3.8, 3.9, 3.10, 3.11) from selection options to ensure compatibility with aaron-common-libs dependency.


## [0.1.6] - 2025-02-20
### Fixed
- pyproject.toml: Replaced "poetry.dev-dependencies" with
  "poetry.group.dev.dependencies".
- post_gen_project.py: Replaced "poetry shell" with eval $(poetry env activate)


## [0.1.5] - 2024-09-25
### Fixed
- Somewhere along the line the file permissions got jacked up.  Removed
  executable permissions off the files.
### Changed
- cookiecutter.json: Removed the @ symbol from the username to allow the
  username to be specified elsewhere in code without prepending the @
  which is only used for GitHub.


## [0.1.4] - 2024-09-17
### Changed
- docker-compose.yml, docker_build.sh: Fixing labels for GitHub Container Registry.


## [0.1.3] - 2024-07-30
### Changed
- README.md: Improved instructions.  How do hyperlinks in Markdown work? :woozy:


## [0.1.2] - 2024-07-30
### Changed
- README.md: Improved instructions for use.
- cookiecutter.json, hooks/post_gen_project.py: Modified to include
  functionality to remove Docker files if they aren't wanted.
- entrypoint.sh: Removed old environment variable artifact.


## [0.1.1] - 2024-07-30
### Added
- cc-python-cli.png: Added unnecessarily long image file.
### Changed
- README.md: Improved instructions for use.


## [0.1.0] - 2024-07-30
### Added
- Beginning a new project.