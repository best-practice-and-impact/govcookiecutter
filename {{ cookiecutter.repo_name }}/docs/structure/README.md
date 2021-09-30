# `{{ cookiecutter.repo_name }}` structure

This page provides information on the repository's structure. The repository's folder
structure is explained here:

```{toctree}
:maxdepth: 2
./data.md
./docs.md
./notebooks.md
./outputs.md
./src.md
./tests.md
```

## Top-level files

Each subsection here contains a brief description about the files at the top-level of
this Git repository.

### `.env`

Environment variables go here, and can be read in by Python using the `python-dotenv` package, and `os.getenv`:

```in script
from dotenv import load_dotenv
import os

#Load the environment variables from the `.env` file, overriding any system
#environment variables
load_dotenv(override=True)

# Example variable
EXAMPLE_VARIABLE = os.getenv("EXAMPLE_VARIABLE")
```

### `.envrc`

Orchestration file to load environment variables from the `.env` and `.secrets` files.
Only used by systems with `direnv` (https://direnv.net/) installed. Environment
variables can be read in by Python using `os.getenv` _without_ using `python-dotenv`:

```in script
import os

# Example variable
EXAMPLE_VARIABLE = os.getenv("EXAMPLE_VARIABLE")
```


### `.flake8`

A configuration file for the `flake8` Python package that provides linting. This file
is based on the [common configuration described in the GDS Way][gds-way-flake8].

### `.gitignore`

A `.gitignore` file to ignore certain files and folders from this Git repository. [See
the contributor guide to modift the `.gitignore` file][docs-updating-gitignore].

{% if cookiecutter.using_R == "Yes" -%}
### `.lintr`

R-specific configuration file for styling R code.

{% endif -%}

### `.pre-commit-config.yaml`

[A pre-commit hook configuration file][docs-pre-commit-hooks].

{% if cookiecutter.using_R == "Yes" -%}
### `.Rprofile`

R-specific initialisation file that runs automatically when starting R.

{% endif -%}

### `.secrets`

A file to store all secrets and credentials as environment variables. [This file is
read-in by `.envrc`](#envrc), when [loading environment variables with the `direnv`
shell extension][direnv], but is not tracked by Git.

### `.secrets.baseline`

[Baseline file for the `detect-secrets` to detect secrets][detect-secrets]. In
conjunction with `pre-commit`, `detect-secrets` prevents secrets from being committed
to the repository. The baseline file flags secret-like data that the user deliberately
wishes to commit the to repository.

### `CODE_OF_CONDUCT.md`

[The Code of Conduct for contributors to this project][code-of-conduct], including
maintainers and `{{ cookiecutter.organisation_handle }}` organisation owners.

### `conftest.py`

File to contain shared fixture functions for the `pytest` tests in the `tests` folder.

### `CONTRIBUTING.md`

The contributing guidelines for this project.

{% if cookiecutter.using_R == "Yes" -%}
### `DESCRIPTION`

R-specific information related to the project including the name, authors and packages
necessary for the project.

{% endif -%}

### `LICENSE`

The licence for this project. Unless stated otherwise, the codebase is released under
the MIT License. This covers both the codebase and any sample code in the
documentation. The documentation is © Crown copyright and available under the terms of
the Open Government 3.0 licence.

### `Makefile`

The `Makefile` contains a set of commands for the `make` utility. Run the `help`
command for further information at the top-level of the Git repository.

```shell
make help
```

### `pyproject.toml`

A file containing Python project settings. This includes configuration settings for:

- [`isort`](#isort)
- [`pytest`](#pytest)
- [code coverage](#code-coverage)

#### `isort`

Python imports are arranged according to the [specification defined by `black`][black].

#### `pytest`

To run the tests within the `tests` folder using the `pytest` Python package, enter
the following command:

```shell
pytest
```

#### Code coverage

To run code coverage using the `coverage` Python package with `pytest`, enter the
following command:

```shell
coverage run -m pytest
coverage html
```

or using the `make` command:

```shell
make coverage_html
```

A code coverage report in HTML will be produced on the code in the `src` folder. This
HTML report can be accessed at `htmlcov/index.html`.

### `README.md`

An overview of the Git repository, including all necessary instructions to run the code.

### `requirements.txt`

A list of Python package requirements for this Git repository, which can be installed
using the `pip install` command.

```shell
pip install --requirement requirements.txt
```

Alternatively, to install the requirements file along with pre-commit hooks, run the
following command:

```shell
make requirements
```

{% if cookiecutter.using_R == "Yes" -%}
### `startup.R`

R-specific file that installs necessary packages specified in the `DESCRIPTION` file
upon starting R using `.Rprofile`.

{% endif -%}

[black]: https://black.readthedocs.io/en/stable/
[code-of-conduct]:../contributor_guide/CODE_OF_CONDUCT.md
[detect-secrets]: https://github.com/Yelp/detect-secrets
[direnv]: https://direnv.net/
[docs-pre-commit-hooks]: ../contributor_guide/pre_commit_hooks.md
[docs-updating-gitignore]: ../contributor_guide/updating_gitignore.md
[gds-way-flake8]: https://gds-way.cloudapps.digital/manuals/programming-languages/python/python.html#common-configuration
