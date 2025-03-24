# `docs` folder overview

All documentation for the project should be included in this folder in MyST Markdown
files, with acceptable formatting for Sphinx. Further details
is supplied in the [contributing guidance][contributing-guidance].

If you want to include any documentation written in the `{{ cookiecutter.repo_name }}`
folder without duplicating it, include it in the `docs/{{ cookiecutter.repo_name }}`
folder.

To build the documentation, run the `docs` command [from `Makefile` using the `make`
utility at the top-level of this repository][docs-makefile].

```shell
make docs
```

or, alternatively, run:

```shell
sphinx-build -b html ./docs ./docs/_build
```

The HTML-version of this documentation can then be viewed at `docs/_build/index.html`,
relative to the top-level of this repository.

[docs-makefile]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/docs/structure/README.md#makefile
[contributing-guidance]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/CONTRIBUTING.md#documentation
