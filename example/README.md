# `example` folder overview

Test builds of the cookiecutter template using all default options can be made in this
repository using the following `make` command:

```{warning}
Any existing folders will be automatically deleted by executing this `make` command.
```

```shell
make example
```

or, alternatively, delete any pre-existing sub-folders in the `example` folder, and run:

```shell
python -m cookiecutter . -o ./example --no-input
```
