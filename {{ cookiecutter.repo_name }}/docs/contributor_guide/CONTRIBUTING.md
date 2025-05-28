# Contributing

We love contributions! We've compiled this documentation to help you understand our
contributing guidelines. Please also read our [`CODE_OF_CONDUCT.md`][code-of-conduct].

[If you still have questions, please contact us][email] and we'd be happy to help!


## Getting started

To start contributing, open your terminal and install the package and
[pre-commit hooks][pre-commit] using:

```shell
pip install -e .[dev]
pre-commit install
```

or use the `make` command:
```shell
make install_dev
```

The pre-commit hooks are a security feature to ensure, for example, no secrets,
large data files, or Jupyter notebook outputs are accidentally committed into the
repository. For more information and common use cases, please refer to a hook's
documentation such as [detect-secrets][detect-secrets-repo] or [nbstripout][nbstripout-repo].

## Code conventions

We mainly follow the [GDS Way][gds-way] in our code conventions. For Python code, we
follow the [GDS Way Python style guide][gds-way-python], and use the flake8
pre-commit hook for linting.

### Git and GitHub

We use Git to version control the source code. Please read
the [Quality assurance of code for analysis and research][duck-book-version-control] for
details on Git best practice. This includes how to write good commit messages, how to
branch appropriately and solve merge conflicts.

The .gitignore used in this repository was created with generic exclusions
from [gitignore.io][gitignore-io].

Pull requests into `main` require at least one approved review.

### Markdown

Local links can be written as normal, but external links should be referenced at the
bottom of the Markdown file for clarity. For example:

Use a local link to reference the [`README.md`](../../README.md) file, but an external
link for [GOV.UK][gov-uk].

We also try to wrap Markdown to a line length of 88 characters, but this is not
strictly enforced in all cases, for example with long hyperlinks.

## Testing

[Tests are written using the `pytest` framework][pytest], with its configuration in the
`pyproject.toml` file. Note, only tests in the `tests` folder are run. To run the
tests, enter the following command in your terminal:

```shell
pytest
```

### Code coverage

Code coverage of Python scripts is measured using the [`coverage` Python
package][coverage]; its configuration can be found in `pyproject.toml`. Note coverage
only extends to Python scripts in the `{{ cookiecutter.repo_name.lower().replace(' ', '_').replace('-', '_') }}` folder.

To run code coverage, and view it as an HTML report, enter the following command in
your terminal:

```shell
coverage run -m pytest
coverage html
```

or use the `make` command:

```shell
make coverage_html
```

The HTML report can be accessed at `htmlcov/index.html`.

## Documentation

Documentation is stored in the `docs` folder unless it's more
appropriate to store it elsewhere, like this contributing guidance. We
write our documentation in [MyST Markdown][myst] for use in [Sphinx][sphinx], to make
a searchable wesite. Public sector websites must be accessible by law, and GOV.UK has
further information on these [requirements][gov-uk-accessibility].

To create the website locally, run the following command in your terminal
at the top-level of this project:

```shell
make docs
```

This should create an HTML version of your documentation accessible from
`docs/_build/index.html`.

[code-of-conduct]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/CODE_OF_CONDUCT.md
[coverage]: https://coverage.readthedocs.io/
[detect-secrets-repo]: https://github.com/Yelp/detect-secrets/tree/master
[duck-book-version-control]: https://best-practice-and-impact.github.io/qa-of-code-guidance/version_control.html
[gds-way-python]: https://gds-way.cloudapps.digital/manuals/programming-languages/python/python.html#python-style-guide
[gds-way]: https://gds-way.digital.cabinet-office.gov.uk/
[gitignore-io]: https://www.toptal.com/developers/gitignore
[gov-uk-accessibility]: https://www.gov.uk/guidance/accessibility-requirements-for-public-sector-websites-and-apps
[gov-uk]: https://www.gov.uk/
[myst]: https://myst-parser.readthedocs.io/
[nbstripout-repo]: https://github.com/kynan/nbstripout
[pre-commit]: https://pre-commit.com
[pytest]: https://docs.pytest.org/
[sphinx]: https://www.sphinx-doc.org/en/master/index.html
