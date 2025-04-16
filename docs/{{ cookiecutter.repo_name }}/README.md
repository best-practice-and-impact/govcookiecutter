# `{{ cookiecutter.repo_name }}` folder structure

This is information about the structure of the created repository contained
in the `{{ cookiecutter.repo_name }}` folder within the `govcookiecutter` repository.
Some of these files may not be present in the actual created repository, as this is
customised based on the user's answers to the prompts on set-ups.

```{toctree}
:maxdepth: 2

./dot_govcookiecutter.md
./docs.md
./tests.md
./source_code.md
```

## Top-level files

### .Rprofile

A user profile to configure R settings, including environment variables.

### .env

A file for storing environment variables.

### .envrc

A file for handing directory-specific environment variables.

### .flake8

A configuration file for the `flake8` Python package that provides linting.

### .gitignore

A `.gitignore` file to specify that git should not track certain files and folders in this repository.

### .lintr

A file specifying the parameters of R linting.

### pre-commit-config.yaml

A pre-commit hook file covering linting, secret detection, and styling among other things.

### .secrets

A file for storing secrets and credentials as environment variables. This file should remain in the `.gitignore`.

### .secrets.baseline

A file for configuration of the  `detect-secrets`[detect-secrets] pre-commit hook. `detect-secrets` prevents secrets from being committed
to the repository. The baseline file flags secret-like data that the user deliberately wishes to commit the to repository.

### CODE_OF_CONDUCT.md

The Code of Conduct describes how contributors should interact with each other on the project.
It also contains information about the responsibilities of contributors both within and outside
of the organisation owning the created repository.

### conftest.py

A file to store shared fixture functions for the `pytest` tests in the `tests` folder.

### CONTRIBUTING.md

The contributing guidelines for this project, explaining how contributors can
engage with the created project.

### DESCRIPTION

An file containing information about R code to include package information, such as dependencies.

### LICENSE

The licence describes how the project can be used or re-used by others. Unless stated otherwise, the codebase is released under
the MIT License.

### make.bat

A file mimicking a Unix/Linux `Makefile` for Windows.

### Makefile

A file containing shortcut commends for Unix/Linux users.

### pyproject.toml

A file for Python package building that includes information such as dependencies. It also configures tools such as
isort, pytest, and bandit.

### README.md

A file containing information about the project, such as requirements and instructions for how to run the code. Can
be editted to add additional information such as a summary of the project.

### setup.cfg

A file containing Python package metadata for use with `setuptools`.

### setup.py

A file to set up the created Python package with `setuptools`.

### startup.R

A file used by R to set up an environment.
