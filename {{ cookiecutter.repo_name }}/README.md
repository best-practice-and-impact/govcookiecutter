# `{{ cookiecutter.repo_name }}`

{{ cookiecutter.overview }}

```{warning}
Where this documentation refers to the root folder we mean where this README.md is
located.
```
## What is `{{ cookiecutter.repo_name }}`?

Add a summary of your project here.

## Getting started

To start using this project, first make sure your system meets its
requirements.

It's suggested that you install this package and its requirements within
a virtual environment.

## Requirements

- Python 3.9+ installed
{% if cookiecutter.using_R == "Yes" -%}
- R 4.2.3+ installed
{% endif -%}
- a `.secrets` file with the required [secrets and credentials](#required-secrets-and-credentials)
- to have [loaded environment variables][docs-loading-environment-variables] from `.env`

Contributors have some additional requirements - please see our [contributing guidance][contributing].

## Installing the package

Whilst in the root folder, in a terminal, you can install the package and its
Python dependencies using:

```shell
python -m pip install -U pip setuptools
pip install -e .
```

{% if cookiecutter.using_R == "Yes" -%}
While in the root folder in an R console, such as that in Rstudio,
install the R components with:
```R
install.packages(".")
```
{% endif -%}

### Install for contributors (Python only)

To install the contributing requirements, use:
```shell
python -m pip install -U pip setuptools
pip install -e .[dev]
pre-commit install
```

This installs an editable version of the package. This means that when you update the
package code you do not have to reinstall it for the changes to take effect.
This saves a lot of time when you test your code.

{% if cookiecutter.using_R == "Yes" -%}
While in the root folder in an R console, such as that in Rstudio, load the package
using `devtools`:
```R
#install.packages("devtools")
devtools::load_all()
```
{% endif -%}

Remember to update the setup and requirement files inline with any changes to your
package.

## Running the pipeline (Python only)

The entry point for the pipeline is stored within the package and called `run_pipeline.py`.
To run the pipeline, run the following code in the terminal (either in the root directory of the
project, or by specifying the path to `run_pipeline.py` from elsewhere).

```shell
python src/{{ cookiecutter.repo_name.lower().replace(' ', '_').replace('-', '_') }}/run_pipeline.py
```

Alternatively, most Python IDEs allow you to run the code directly using a `run` button.

## Required secrets and credentials

To run this project, you need a `.secrets` file with [secrets/credentials as
environmental variables][docs-loading-environment-variables-secrets]. The
secrets/credentials should have the following environment variable name(s):

| Secret/credential | Environment variable name | Description                                |
|-------------------|---------------------------|--------------------------------------------|
| Secret 1          | `SECRET_VARIABLE_1`       | Plain English description of Secret 1.     |
| Credential 1      | `CREDENTIAL_VARIABLE_1`   | Plain English description of Credential 1. |

Once you've added them, [load these environment variables][docs-loading-environment-variables] using
`.env`.

## Project structure layout

The cookiecutter template generated for each project will follow this folder structure:

```shell
.
├── {{ cookiecutter.repo_name }}/
│   └── {{ cookiecutter.repo_name.lower().replace(' ', '_').replace('-', '_') }}/
│       ├── example_modules/
│       │   ├── __init__.py
│       │   └── example_module.py
│       ├── __init__.py
│       ├── example_config.yml
│       └── run_pipeline.py
└── ...
```

## Licence

Unless stated otherwise, the codebase is released under the MIT License. This covers
both the codebase and any sample code in the documentation. The documentation is ©
Crown copyright and available under the terms of the Open Government 3.0 licence.

## Contributing

If you want to help us build and improve `{{ cookiecutter.repo_name }}`, please take a look at our
[contributing guidelines][contributing].

## Acknowledgements

This project structure is based on the [`govcookiecutter` template project][govcookiecutter].

[contributing]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/CONTRIBUTING.md
[govcookiecutter]: https://github.com/best-practice-and-impact/govcookiecutter
[docs-loading-environment-variables]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/user_guide/loading_environment_variables.md
[docs-loading-environment-variables-secrets]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/user_guide/loading_environment_variables.md#storing-secrets-and-credentials
