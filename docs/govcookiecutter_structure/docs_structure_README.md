# `govcookiecutter` structure

This page provides information on the `govcookiecutter` repository structure.
Further detail on folder contents is available:

```{toctree}
:maxdepth: 1
./docs.md
./example.md
./hooks.md
./tests.md
../{{ cookiecutter.repo_name }}/docs_repo_README.md
```

## Top-level files

Each subsection here contains a brief description about the files at the top-level of
this Git repository.

### `.flake8`

A configuration file for the `flake8` Python package that provides linting. This file
is based on the common configuration described in the [GDS Way][gds-way-flake8].

### `.gitignore`

A `.gitignore` file to specify that git should not track certain files and folders in this repository.

### `.pre-commit-config.yaml`

A [pre-commit hook][docs-pre-commit-hooks] file covering linting, secret detection,
and styling among other things.

### `.secrets.baseline`

A file for configuration of the  `detect-secrets`[detect-secrets] pre-commit hook. `detect-secrets` prevents secrets from being committed
to the repository. The baseline file flags secret-like data that the user deliberately wishes to commit the to repository.

### `CHANGELOG.md`

A file describing the changes made to `govcookiecutter` over time, including unreleased
and upcoming changes.

### `CODE_OF_CONDUCT.md`

The [Code of Conduct][code-of-conduct] describes how contributors should interact
with each other on the project.
It also contains information about the responsibilities of contributors
both within and outside of the `best-practice-and-impact` organisation.

### `conftest.py`

A file to store shared fixture functions for the `pytest` tests in the `tests` folder.

### `CONTRIBUTING.md`

The contributing guidelines for this project, explaining how contributors can
engage with `govcookiecutter`.

### `cookiecutter.json`

A file containing the prompts for template generation alongside default values.
Any keys beginning with an underscore are not shown to users.

The first block of JSON refers to cookiecutter extensions. The next block relates to
organisation-specific information, such as a user's HM Government department, and its
organisation handle on GitHub or GitLab. The last block relates to project-specific
information.

For further information in the `cookiecutter.json` file, see the `cookiecutter`
package [documentation][cookiecutter].

### `LICENSE`

The licence describes how the project can be used or re-used by others. Unless stated otherwise, the codebase is released under
the MIT License. This covers both the codebase and any sample code in the
documentation. The documentation is © Crown copyright and available under the terms of
the Open Government 3.0 licence.

### `Makefile`

The `Makefile` contains a set of commands for the `make` utility, more often
used on Unix-like and Linux systems. This allows a user to, for example,
run the `help` command for further information at the top-level of the Git repository.

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

To run the tests within the `tests`, and `{{ cookiecutter.repo_name }}/tests` folders
using the `pytest` Python package, enter the following command:

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

Unix and Linux users can use the `make` command:

```shell
make coverage_html
```

A code coverage report in HTML will be produced on the code in the `hooks` and
`{{ cookiecutter.repo_name }}/{{ cookiecutter.repo_name.lower().replace(' ', '_').replace('-', '_') }}` folders.
This HTML report can be accessed at `htmlcov/index.html`.

### `README.md`

An overview of the Git repository and aims of `govcookiecutter`, including all necessary instructions to run the code.

### `requirements.txt`

A list of Python package dependencies for the `govcookiecutter` repository,
which can be installed using the `pip install` command:

```shell
pip install --requirement requirements.txt
```

Alternatively, Unix and Linux users can install the requirements along with pre-commit hooks by running the following command:

```shell
make requirements
```

[black]: https://black.readthedocs.io/en/stable/
[code-of-conduct]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/docs/CODE_OF_CONDUCT.md
[cookiecutter]: https://cookiecutter.readthedocs.io/
[detect-secrets]: https://github.com/Yelp/detect-secrets
[docs-pre-commit-hooks]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/CONTRIBUTING.md#getting-started
[gds-way-flake8]: https://gds-way.cloudapps.digital/manuals/programming-languages/python/python.html#common-configuration
