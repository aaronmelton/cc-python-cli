# CHANGELOG


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