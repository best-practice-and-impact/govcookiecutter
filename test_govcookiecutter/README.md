# `test_govcookiecutter`

The task is to review the Contributing guide of the govcookiecutter project on Github.

```{warning}
Where this documentation refers to the root folder we mean where this README.md is
located.
```

## Getting started

To start using this project, [first make sure your system meets its
requirements](#requirements).

It's suggested that you install this pack and it's requirements within a virtual environment.

## Installing the package (Python Only)

Whilst in the root folder, in the command prompt, you can install the package and it's dependencies
using:

```shell
python -m pip install -U pip setuptools
pip install -e .
```
or use the `make` command:
```shell
make install
```

This installs an editable version of the package. Meaning, when you update the
package code, you do not have to reinstall it for the changes to take effect.
(This saves a lot of time when you test your code)

Remember to update the setup and requirement files inline with any changes to your
package. The inital files contain the bare minimum to get you started.

## Running the pipeline (Python only)

The entry point for the pipeline is stored within the package and called `run_pipeline.py`.
To run the pipeline, run the following code in the terminal (whilst in the root directory of the
project).

```shell
python src/test_govcookiecutter/run_pipeline.py
```

Alternatively, most Python IDE's allow you to run the code directly from the IDE using a `run` button.

## Required secrets and credentials

To run this project, [you need a `.secrets` file with secrets/credentials as
environmental variables][docs-loading-environment-variables-secrets]. The
secrets/credentials should have the following environment variable name(s):

| Secret/credential | Environment variable name | Description                                |
|-------------------|---------------------------|--------------------------------------------|
| Secret 1          | `SECRET_VARIABLE_1`       | Plain English description of Secret 1.     |
| Credential 1      | `CREDENTIAL_VARIABLE_1`   | Plain English description of Credential 1. |

Once you've added, [load these environment variables using
`.env`][docs-loading-environment-variables].

## Licence

Unless stated otherwise, the codebase is released under the MIT License. This covers
both the codebase and any sample code in the documentation. The documentation is ©
Crown copyright and available under the terms of the Open Government 3.0 licence.

## Contributing

[If you want to help us build, and improve `test_govcookiecutter`, view our
contributing guidelines][contributing].

### Requirements

[```Contributors have some additional requirements!```][contributing]

- Python 3.6.1+ installed
- a `.secrets` file with the [required secrets and
  credentials](#required-secrets-and-credentials)
- [load environment variables][docs-loading-environment-variables] from `.env`

To install the contributing requirements, open your terminal and enter:
```shell
python -m pip install -U pip setuptools
pip install -e .[dev]
pre-commit install
```
or use the `make` command:
```shell
make install_dev
```

## Acknowledgements

[This project structure is based on the `govcookiecutter` template
project][govcookiecutter].

[contributing]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/CONTRIBUTING.md
[govcookiecutter]: https://github.com/best-practice-and-impact/govcookiecutter
[docs-loading-environment-variables]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/user_guide/loading_environment_variables.md
[docs-loading-environment-variables-secrets]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/user_guide/loading_environment_variables.md#storing-secrets-and-credentials
