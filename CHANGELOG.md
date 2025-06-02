# Changelog

All notable changes to this project will be documented in this file, grouped by Added, Fixed, Changed, and Removed.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased] -

### Added

### Fixed

### Changed

### Removed

## [2.1.0] - 2nd June 2025

### Added

- Example test and module
- Example pipeline
- Version to config
- Dev dependencies to config
- New requirements: `bandit` and `jinja2-time`
- `bandit` to user pre-commit hooks
- Including common Excel file times in the default .gitignore
- `bandit` to dev pre-commit hooks
- R install guidance to template README
- Setup question for locked down environments, uses local installed packages for commit hooks

### Fixed

- Broken links

### Changed

- Updated instructions on running the tests
- Updated imports
- Exclude certain files from pre-commit hooks
- Updated README to use `python -m`
- Minor contributing guidance changes
- Updated Python versions to 3.9-3.12
- Updated Python versions in workflows to 3.9-3.12
- Updated dev pre-commit hook versions via `pre-commit autoupdate`
- Template code of conduct updated
- Template contributing guidance updated
- Updated README
- Updated documentation website for `govcookiecutter` and created repo structures

### Removed

- Example data folder
- Removed the Email Address prompts from the installation.

## [2.0.0] - 6th March 2023

### Added

- Workflow to check external links on pull request

### Fixed

- Broken links

### Changed

- Updated folder structure
- Relative links have been replaced with complete paths
- Workflow actions now use later versions
- Updated CRAN link being installed from in startup.R
- Updates to the Contributing Guidance

### Removed

- Workflow support for Python 3.6


[unreleased]: https://github.com/best-practice-and-impact/govcookiecutter
[2.1.0]: https://github.com/best-practice-and-impact/govcookiecutter/tree/2.1.0
[2.0.0]: https://github.com/best-practice-and-impact/govcookiecutter/tree/2.0.0
