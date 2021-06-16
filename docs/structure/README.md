# `govcookiecutter` structure

This page provides information on the repository's structure. The repository's folder
structure is explained here:

```{toctree}
:maxdepth: 2
./docs.md
./example.md
./hooks.md
./tests.md
./{{ cookiecutter.repo_name }}.md
```

## Top-level files

Each subsection here contains a brief description about the files at the top-level of
this Git repository.

### `.flake8`

A configuration file for the `flake8` Python package that provides linting. This file
is based on the [common configuration described in the GDS Way][gds-way-flake8].

### `.gitignore`

A `.gitignore` file to ignore certain files and folders from this Git repository. [See
the contributor guide to modift the `.gitignore` file][docs-updating-gitignore].

### `.pre-commit-config.yaml`

[A pre-commit hook configuration file][docs-pre-commit-hooks].

### `.secrets.baseline`

[Baseline file for the `detect-secrets` to detect secrets][detect-secrets]. In
conjunction with `pre-commit`, `detect-secrets` prevents secrets from being committed
to the repository. The baseline file flags secret-like data that the user deliberately
wishes to commit the to repository.

### `CODE_OF_CONDUCT.md`

[The Code of Conduct for contributors to this project][code-of-conduct], including
maintainers and `ukgovdatascience` organisation owners.

### `conftest.py`

File to contain shared fixture functions for the `pytest` tests in the `tests` folder.

### `CONTRIBUTING.md`

The contributing guidelines for this project.

### `cookiecutter.json`

A JSON file containing the prompts and default values during template generation. Note
any keys beginning with an underscore are not shown to users.

The first block of JSON refers to cookiecutter extensions. The next block relates to
organisation-specific information, such as your HM Government department, and its
organisation handle on GitHub or GitLab. The last block relates to project-specific
information.

[For further information in the `cookiecutter.json` file, see the `cookiecutter`
package documentation][cookiecutter].

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
- [Code coverage](#code-coverage)

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

or using the `make` command:

```shell
make coverage_html
```

A code coverage report in HTML will be produced on the code in the `hooks`, and the
`{{ cookiecutter.repo_name }}/src` folders. This HTML report can be accessed at
`htmlcov/index.html`.

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

[black]: https://black.readthedocs.io/en/stable/
[code-of-conduct]: ../CODE_OF_CONDUCT.md
[cookiecutter]: https://cookiecutter.readthedocs.io/
[detect-secrets]: https://github.com/Yelp/detect-secrets
[docs-pre-commit-hooks]: ../%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/pre_commit_hooks.md
[docs-updating-gitignore]: ../%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/updating_gitignore.md
[gds-way-flake8]: https://gds-way.cloudapps.digital/manuals/programming-languages/python/python.html#common-configuration
