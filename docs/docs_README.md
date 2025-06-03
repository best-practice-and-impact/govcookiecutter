# `docs` folder overview

This folder contains documentation for `govcookiecutter`. These are written in MyST Markdown files with Sphinx compatibility.

```{warning}
Further details to consider when modifying these files are supplied in the [contributing guidance][contributing-guidance].
```

To include documentation from the `{{ cookiecutter.repo_name }}`
folder without duplicating it, refer to it in a file within the `docs/{{ cookiecutter.repo_name }}` folder.

To build the documentation, run:

```shell
sphinx-build -b html ./docs ./docs/_build
```

Unix and Linux users can alternatively run the `docs` command from [`Makefile`][docs-makefile] using
the `make` utility at the top-level of this repository.

```shell
make docs
```

The HTML-version of this documentation can then be viewed at `docs/_build/index.html`,
relative to the top-level of this repository.

[docs-makefile]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/docs/govcookiecutter_structure/docs_structure_README.md#makefile
[contributing-guidance]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/CONTRIBUTING.md#documentation
