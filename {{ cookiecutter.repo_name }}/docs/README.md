# `docs` folder overview

All documentation for the project should be included in this folder in either
reStructuredText or Markdown files, with acceptable formatting for Sphinx. [Guidance on
how to write Sphinx documentation is supplied in the contributor
guide][writing-sphinx-documentation].

To build the documentation, run the `docs` command [from `Makefile` using the `make`
utility at the top-level of this repository][docs-makefile].

```shell
make docs
```

or, alternatively, run:

```shell
sphinx-build -b linkcheck ./docs ./docs/_build
```

The HTML-version of this documentation can then be viewed at `docs/_build/index.html`,
relative to the top-level of this repository.

## Analytical quality assurance (AQA)

All analytical quality assurance (AQA) documents can be found in the `docs/aqa` folder.
These files document how this project meets organisational [guidance on producing
quality analysis for HM Government projects][aqua-book].

[aqua-book]: https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government
[docs-makefile]: ../docs/structure/README.md#makefile
[writing-sphinx-documentation]: ../docs/contributor_guide/writing_sphinx_documentation.md
