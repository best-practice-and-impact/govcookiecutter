# `docs` folder

All documentation for the project should be included in this folder in MyST Markdown
files, with acceptable formatting for Sphinx.

To build the documentation, run the `docs` command from the [`Makefile`][docs-makefile]
using the `make` utility at the top-level of this Git repository.

```shell
make docs
```

Guidance on how to write Sphinx documentation is supplied in the
[contributor guide][writing-sphinx-documentation]. If you want to include any
documentation written in the `{{ cookiecutter.repo_name }}` folder without duplicating
it, include it in the `docs/{{ cookiecutter.repo_name }}` folder.

[docs-makefile]: ../docs/structure/README.md#makefile
[writing-sphinx-documentation]: ../%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/writing_sphinx_documentation.md
