# Project structure

The project is set up with the following structure:

* [Folders](#folder-structure)
    * [`data`](#data-folder)
    * [`docs`](#docs-folder)
    * [`notebooks`](#notebooks-folder)
    * [`outputs`](#outputs-folder)
    * [`src`](#src-package)
    * [`tests`](#tests-folder)
* [Top-level files](#top-level-files)
    * [`.envrc`](#envrc)
    * [`.flake8`](#flake8)
    * [`.gitignore`](#gitignore)
    {%- if cookiecutter.create_secrets_file == "Yes" %}
    * [`.secrets`](#secrets){% endif %}
    * [`Makefile`](#makefile)
    * [`README.md`](#readmemd)
    * [`requirements.txt`](#requirementstxt)

## Folder structure

Each subsection here contains a brief description about the suggested usage of these folders.

### `data` folder

Any data that needs to be stored locally should be saved in this location. This folder, and all its sub-folders are not
version-controlled.

The sub-folders should be used as follows:

* `external`: Any data that will **not** be processed at all, such as reference data;
* `raw`: Any raw data before any processing;
* `interim`: Any raw data that has been partially processed and, for whatever reason, needs to be stored before further 
processing is completed; and
* `processed`: Any raw or interim data that has been fully processed into its final state.

The folder paths for these directories are loaded as environment variables by the [`.envrc`](#envrc) file; to load them
in Python, use any or all of the following code:

```python
import os

DIR_DATA = os.environ.get("DIR_DATA")
DIR_DATA_EXTERNAL = os.environ.get("DIR_DATA_EXTERNAL")
DIR_DATA_RAW = os.environ.get("DIR_DATA_RAW")
DIR_DATA_INTERIM = os.environ.get("DIR_DATA_INTERIM")
DIR_DATA_PROCESSED = os.environ.get("DIR_DATA_PROCESSED")
```

### `docs` folder

All documentation for the project should be included in this folder in either Markdown or ReStructuredText files, with 
acceptable formatting for Sphinx.

To build the documentation, run the `docs` command from the [`Makefile`](#makefile) using the `make` utility at the 
top-level of this Git repository.

```shell script
make docs
```

### `notebooks` folder

All Jupyter notebooks should be stored in this folder. The [`.envrc`](#envrc) file should automatically add the entire
project path into the `PYTHONPATH` environment variable - this should allow you to directly import `src` in your 
notebook.

### `outputs` folder

All outputs from the project should be stored here. This folder path for these directories is loaded as an environment 
variable by the [`.envrc`](#envrc) file; to load them in Python, use the following code:

```python
import os

DIR_OUTPUT = os.environ.get("DIR_OUTPUT")
```

### `src` package

All functions for this project, should be stored in this folder. **All tests should be stored in the 
[`tests`](#tests-folder) folder**, which is one-level above this folder in the main project directory.

The sub-folders should be used as follows:

    * `make_data`: Data processing-related functions;
    * `make_features`: Feature-related functions, for example, functions to create features from processed data;
    * `make_models`: Model-related functions;
    * `make_visualisations`: Functions to produce visualisations;
    * `utils`: Utility functions that are helpful in the project.

It is strongly suggested that you import functions in the `src/__init__.py` script, and that you try 
and use absolute imports within `src` scripts whenever possible.

### `tests` folder

All tests for the functions defined in the [`src`](#src-folder) package should be stored here.

## Top-level files

Each subsection here contains a brief description about the files at the top-level of this Git repository.

### `.envrc`

A file containing environment variables for the Git repository that can be selectively loaded. This uses the 
[`direnv`](https://direnv.net/) shell extension; see their documentation for further information.

### `.flake8`

A configuration file for the [`flake8`](https://gitlab.com/pycqa/flake8) Python package that provides linting. This 
file is based on the
[common configuration](https://gds-way.cloudapps.digital/manuals/programming-languages/python/python.html#common-configuration) 
described on [The GDS Way](https://gds-way.cloudapps.digital).

### `.gitignore`

A `.gitignore` file to ignore certain files and folders from this Git repository. See the 
[GitHub Help pages](https://help.github.com/en/github/using-git/ignoring-files) for further information.
{% if cookiecutter.create_secrets_file == "Yes" %}
### `.secrets`

A file to store all secrets and credentials as environment variables. This is read-in by [`.envrc`](#envrc) using the 
[`direnv`](https://direnv.net/) shell extension, but is **not** tracked by Git.
{% endif %}
### `Makefile`

The `Makefile` contains a set of commands for the `make` utility. Run the `help` command for further information at the 
top-level of the Git repository.

```shell script
make help
```

### `README.md`

An overview of the Git repository, including all necessary instructions to execute the code.

### `requirements.txt`

A list of Python package requirements for this Git repository, which can be installed using the `pip install` command.

```shell script
pip install --requirement requirements.txt
``` 
