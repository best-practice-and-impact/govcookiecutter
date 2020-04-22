# {{ cookiecutter.project_name }}

## Overview

{{ cookiecutter.overview }}

## Requirements

To run the code in this GitHub repository, please make sure your system meets the following requirements:

* Unix-like operating system (macOS, Linux, …);
* [`direnv`](https://direnv.net/) installed, including shell hooks;
* [`.envrc`](.envrc) allowed/trusted by `direnv` to use the environment variables - see 
[below](#allowingtrusting-envrc);
{%- if cookiecutter.create_secrets_file == "Yes" %}
* If missing, [create a `.secrets` file](#creating-a-secrets-file) to store untracked secrets;{% endif %}
* Python 3.5 or above; and
* Python packages installed from the `requirements.txt` file.

Note there may be some Python IDE-specific requirements around loading environment variables, which are not considered 
here.

### Allowing/trusting `.envrc`

To allow/trust the [`.envrc`](.envrc) run the `allow` command using `direnv` at the top level of this repository.

```shell script
direnv allow
```
{% if cookiecutter.create_secrets_file == "Yes" %}
### Creating a `.secrets` file

Secrets used by this repository can be stored in a `.secrets` file. **This is not tracked by Git**, and so secrets will 
not be committed onto your remote.

In your shell terminal, at the top level of the repository, create a `.secrets` file.

```shell script
touch .secrets
```

Open this new `.secrets` file using a text editor, and add any secrets as environmental variables. For example, to add 
a JSON credentials file for Google BigQuery, add the following code to `.secrets`.

```shell script
export GOOGLE_APPLICATION_CREDENTIALS="path/to/credentials.json"
```
{% endif %}
### Installing Python packages

To install required Python packages via `pip`, run the following `make` command at the top level of this repository:

```shell script
make requirements
```

## Folder structure

An overview of the folder structure, and the top-level files can be found [here](docs/structure/README.md).
