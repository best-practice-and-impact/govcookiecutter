# [WIP] govcookiecutter
A cookiecutter template for data science projects within UK Government.

This repository is under development - please use the 
[`cookiecutter-data-science-gds`](https://github.com/ukgovdatascience/cookiecutter-data-science-gds) cookiecutter 
template for now!

## Requirements

This project runs on Python 3.5+. To install required Python packages via `pip`, first [set up a Python virtual 
environment](#creating-a-python-virtual-environment); this ensures you do not install the packages globally. Note there 
are additional [requirements](./%7B%7B%20cookiecutter.repo_name%20%7D%7D/README.md#requirements) for the output.

To create a new repository structure from this cookiecutter, install the required Python packages via `pip` by running 
the following command:

```shell script
make requirements
```

To make developments to this project, install the development Python packages via `pip` using:

```shell script
make requirements-dev
```

### Creating a Python virtual environment

Creating a Python virtual environment depends on whether you are using [base Python](#base-python-interpreter) or 
[Anaconda](#anaconda-interpreter) as your interpreter.

#### Base Python interpreter

If you are using base Python, there are multiple ways to create virtual environments in Python using `pip`, including 
(but not limited to):

* [`venv`](https://docs.python.org/3/tutorial/venv.html);
* [`virtualenv`](https://virtualenv.pypa.io/en/stable/);
* [`pipenv`](https://github.com/pypa/pipenv); and 
* [`pyenv`](https://github.com/pyenv/pyenv) with its `virtualenv` [plugin](https://github.com/pyenv/pyenv-virtualenv).

Follow the documentation of your chosen method to create a Python virtual environment.

#### Anaconda interpreter

If you are using [Anaconda or `conda`](https://www.anaconda.com/), following their 
[documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) to set up a 
conda environment.

## Creating a new project

To create a new project using this template, in the folder where you want your project to be located, run the following 
code in your terminal:

```shell script
cookiecutter https://github.com/ukgovdatascience/govcookiecutter
```

Then following the prompts in your terminal to create the project structure.

## Acknowledgements

This template is based off the 
[DrivenData Cookiecutter Data Science](http://drivendata.github.io/cookiecutter-data-science/) project, especially 
around the `data` and `src` folder structures, and the `make help` command.
