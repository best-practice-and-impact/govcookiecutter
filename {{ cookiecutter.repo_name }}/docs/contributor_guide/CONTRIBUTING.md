# Contributing

We love contributions! We've compiled this documentation to help you understand our
contributing guidelines. [If you still have questions, please contact us][email] and
we'd be happy to help!

## Code of Conduct

[Please read `CODE_OF_CONDUCT.md` before contributing][code-of-conduct].

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

The pre-commit hooks are a security feature to ensure, for example, no secrets[^1],
large data files, and Jupyter notebook outputs are accidentally committed into the
repository. [For more information on pre-commit hooks see our
documentation][docs-pre-commit-hooks].

[^1]: [Only secrets of specific patterns are detected by the pre-commit
      hooks][docs-pre-commit-hooks-secrets-definition].

## Code conventions

[We mainly follow the GDS Way in our code conventions][gds-way].

### Git and GitHub

We use Git to version control the source code. [Please read the Quality assurance of code for analysis and research for details on Git best practice][duck-book-version-control]. This includes how to write good commit messages, how to branch correctly and solving merge conflicts.

[If you want to modify the `.gitignore` files, see the template
documentation][docs-updating-gitignore] for further details.

Our source code is stored on {{ cookiecutter.repository_hosting_platform }}. Pull requests into `main` require at least one
approved review.

### Python

For Python code, [we follow the GDS Way Python style guide][gds-way-python] with a line
length of 88; the flake8 pre-commit hook should help with this!

### Markdown

Local links can be written as normal, but external links should be referenced at the
bottom of the Markdown file for clarity. For example:

Use a [local link to reference the `README.md`](../../README.md) file, but [an external
link for GOV.UK][gov-uk].

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

[Code coverage of Python scripts is measured using the `coverage` Python
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

[We write our documentation in MyST Markdown for use in Sphinx][myst]. This is mainly
stored in the `docs` folder, unless it's more appropriate to store it elsewhere, like
this file.

[Please read our guidance on how to write accessible
documentation][docs-write-accessible-documentation], as well as our [guidance on
writing Sphinx documentation][docs-write-sphinx-documentation]. This allows you to
build the documentation into an accessible, searchable website.

[code-of-conduct]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/CODE_OF_CONDUCT.md
[coverage]: https://coverage.readthedocs.io/
[docs-pre-commit-hooks]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/pre_commit_hooks.md
[docs-pre-commit-hooks-secrets-definition]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/pre_commit_hooks.md#definition-of-a-secret-according-to-detect-secrets
[docs-updating-gitignore]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/updating_gitignore.md
[docs-write-accessible-documentation]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/writing_accessible_documentation.md
[docs-write-sphinx-documentation]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/writing_sphinx_documentation.md
[gds-way]: https://gds-way.cloudapps.digital/
[duck-book-version-control]: https://best-practice-and-impact.github.io/qa-of-code-guidance/version_control.html
[gds-way-python]: https://gds-way.cloudapps.digital/manuals/programming-languages/python/python.html#python-style-guide
[myst]: https://myst-parser.readthedocs.io/
[pre-commit]: https://pre-commit.com
[pytest]: https://docs.pytest.org/
[gov-uk]: https://www.gov.uk/
[email]: mailto:{{ cookiecutter.contact_email }}
