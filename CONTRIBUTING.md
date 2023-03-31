# Contributing

We love contributions! We've compiled this documentation to help you understand our
contributing guidelines. [If you still have questions, please contact us][email] and
we'd be happy to help!

## Code of Conduct

[Please read `CODE_OF_CONDUCT.md` before contributing][code-of-conduct].

## Getting started

To start contributing, install the required Python packages, and [pre-commit
hooks][pre-commit] using:

```shell
pip install -r requirements.txt
pre-commit install
```

or the `make` command:

```shell
make requirements
```

The pre-commit hooks are a security feature to ensure, for example, no secrets[^1], and
large data files are accidentally committed into the repository. [For more information
on pre-commit hooks see our documentation][docs-pre-commit-hooks].

[^1]: [Only secrets of specific patterns are detected by the pre-commit
      hooks][docs-pre-commit-hooks-secrets-definition].

## Code conventions

[We mainly follow the GDS Way in our code conventions][gds-way].

### Git and GitHub

We use Git to version control the source code. [Please read the GDS Way for details on
Git best practice][gds-way-git]. This includes how to write good commit messages, use
`git rebase` for local branches and `git merge --no-ff` for merges, as well as using
`git push --force-with-lease` instead of `git push -f`.

[If you want to modify the `.gitignore` files, see the template
documentation][docs-updating-gitignore] for further details.

Our source code is stored on GitHub at
[https://github.com/best-practice-and-impact/govcookiecutter][govcookiecutter]. Pull
requests into `main` require at least one approved review.

### Python

For Python code, [we follow the GDS Way Python style guide][gds-way-python] with a line
length of 88; the flake8 pre-commit hook should help with this!

### Markdown

To keep the file uniform, all links should be referenced at the bottom of the markdown
file. This also helps to keep the markdown file organised.

We also try to wrap Markdown to a line length of 88 characters. This is not strictly
enforced in all cases, for example with long hyperlinks.

## Testing

[Tests are written using the `pytest` framework][pytest], with its configuration in the
`pyproject.toml` file. Note, only tests in the `tests`, and
`{{ cookiecutter.repo_name }}/tests` folders folder are run. To run the tests, enter
the following command in your terminal:

```shell
pytest
```

### Code coverage

[Code coverage of Python scripts is measured using the `coverage` Python
package][coverage]; its configuration can be found in `pyproject.toml`. Note coverage
only extends to Python scripts in the `hooks`, and
`{{ cookiecutter.repo_name }}/src` folders.

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

[code-of-conduct]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/CODE_OF_CONDUCT.md
[coverage]: https://coverage.readthedocs.io/
[docs-pre-commit-hooks]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/pre_commit_hooks.md
[docs-pre-commit-hooks-secrets-definition]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/pre_commit_hooks.md#definition-of-a-secret-according-to-detect-secrets
[docs-updating-gitignore]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/updating_gitignore.md
[docs-write-accessible-documentation]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/writing_accessible_documentation.md
[docs-write-sphinx-documentation]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/writing_sphinx_documentation.md
[email]: mailto:gsshelp@statistics.gov.uk
[gds-way]: https://gds-way.cloudapps.digital/
[gds-way-git]: https://gds-way.cloudapps.digital/standards/source-code.html
[gds-way-python]: https://gds-way.cloudapps.digital/manuals/programming-languages/python/python.html#python-style-guide
[govcookiecutter]: https://github.com/best-practice-and-impact/govcookiecutter
[myst]: https://myst-parser.readthedocs.io/
[pre-commit]: https://pre-commit.com/
[pytest]: https://docs.pytest.org/
