# [WIP] govcookiecutter
A cookiecutter template for data science projects within UK Government.

This repository is under development - please use the 
[`cookiecutter-data-science-gds`](https://github.com/ukgovdatascience/cookiecutter-data-science-gds) cookiecutter 
template for now!

## Requirements

This cookiecutter runs on Python 3.5+, and there are additional 
[requirements](./%7B%7B%20cookiecutter.repo_name%20%7D%7D/README.md#requirements) for the output.

To create a new repository structure from this cookiecutter, install the required Python packages via `pip` by running 
the following command:

```shell script
make requirements
```

To make developments to this project, install the development Python packages via `pip` using:

```shell script
make requirements-dev
```

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
