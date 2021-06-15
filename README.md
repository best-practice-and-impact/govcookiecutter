# `govcookiecutter`

A cookiecutter template for analytical, code-based projects within Her Majesty's
Government, and wider public sector.

## Who/what is this for?

> ℹ️ Want to learn more? Want to see `govcookiecutter` in action? Check out this
> [presentation and demo][youtube] from March 2021!

This template is for any public sector analyst(s) who codes! It's main purpose is to:

1. Provide a lightweight, Agile-like approach to Analytical Quality Assurance (AQA)
2. Help quickly set up standardised project structures.

For more information about AQA, see [The Aqua Book][aqua-book], and its
[resources][aqua-book-resources].

Rather than using different files and locations to store AQA and documentation, our
intention is to centralise as much of this as possible onto your Git repository hosting
platform, e.g. GitHub or GitLab.

We use nudges, such as checklists in pull/merge requests, to minimise the burden on
contributors and reviewers to complete AQA checks. This results in faster iterative
development and deployment, whilst ensuring organisation-wide standards on assurance
are met.

We have also included [pre-commit hooks][pre-commit] to prevent accidental committing
of secrets[^1], large data files, and Jupyter notebook outputs
for security purposes.

[^1]: [Only secrets of specific patterns are detected by the pre-commit
hooks][docs-pre-commit-hooks-secrets-definition].

## Getting started with `govcookiecutter` for your projects

> ⚠️ Full functionality is only available for Unix-based systems (macOS, Linux, ...).
> For Windows systems, you will need your own way of handling secrets, and will not
> have access to helper commands in the `Makefile`; further details are available in
> this [issue][issue-windows-os]!

> ⚠️ Python or Python with R projects for GitHub or GitLab are supported — feel free to
> [contribute](#contributing) to support other operating systems/programming languages!

> ℹ️ See a live demo [here][youtube-creation]!

To use this template to start your next coding project, make sure your system meets the
[requirements](#requirements-to-create-a-cookiecutter-template).

Once you're all set up, open your terminal, navigate to the directory where you want
your new repository to exist, and run the following commands:

```shell
cookiecutter https://github.com/ukgovdatascience/govcookiecutter
```

Follow the prompts, and that's it — you've created your project structure!
Post-creation, there are a few [mandatory changes](#changes-to-make-post-creation) to
make, as well as a some [optional changes](#changes-to-consider-post-creation) you
should also consider making.

Otherwise, that's it — happy coding! 🎉

### Requirements to create a cookiecutter template

> ℹ️ Contributors have some additional requirements! Check out the
> [contributing guidelines][contributing] for further details.

To get started your system should meet the following requirements:

1. Python 3.6.1+ installed
2. R 4.0.4+ installed (optional)[^2]
3. The [`cookiecutter` package installed](#installing-cookiecutter)

[^2]: Only for combined Python and R projects, if selected in the prompts during
project creation.

#### Installing cookiecutter

There are many ways to install the [`cookiecutter`][cookiecutter] package. **Our
recommendation is to install it at the system or user level**, rather than as a Python
package via `pip` or `conda`. This ensures it is isolated from the rest of your system,
and always available.

For macOS, open your terminal, and install `cookiecutter` via [Homebrew][homebrew]:

```shell
brew install cookiecutter
```

For Debian/Ubuntu, use the following commands:

```shell
sudo apt-get install cookiecutter
```

> ℹ️ We assume your `python` command loads Python 3.6+!

Otherwise, you can install `cookiecutter` via `pip` — you may wish to create a virtual
environment first:

```shell
python -m pip install --user cookiecutter
```

## Changes to make post-creation

Here's a few changes you **must** do once you've created your new project:

- Set up a Python virtual environment — there are **many** ways to [set up a virtual
  environment][pluralsight], so we'll let you decide what's best for you!
- Git is not set up by default — open your terminal, navigate to your new project, run
  `git init` in your shell to set it up.
- Install the packages necessary by running `make requirements` in your shell.

## Changes to consider post-creation

Here's a few changes you should consider changing once you've created your new project:

- Make sure the `README.md` reflects what **you** want to do with your project!
- Have a look inside the `docs/aqa` folder; you may want to modify some of them, e.g.
  the AQA plan
- Want to add some project-specific checklists to the pull/merge request template? See
  the relevant Markdown files within the `.github` (GitHub) or
  `.gitlab/merge_request_templates` (GitLab) folder

## Licence

Unless stated otherwise, the codebase is released under the MIT License. This covers
both the codebase and any sample code in the documentation. The documentation is ©
Crown copyright and available under the terms of the Open Government 3.0 licence.

## Contributing

If you want to help us build, and improve `govcookiecutter`, view our [contributing
guidelines][contributing].

## Acknowledgements

This template is based off the [DrivenData Cookiecutter Data Science][drivendata]
project, especially around the template data and src folder structures, and the
`make help` commands in the Makefiles.

[aqua-book]: https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government
[aqua-book-resources]: https://www.gov.uk/government/collections/aqua-book-resources
[docs-pre-commit-hooks-secrets-definition]: ./%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/pre_commit_hooks.md#definition-of-a-secret-according-to-detect-secrets
[contributing]: ./CONTRIBUTING.md
[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[drivendata]: http://drivendata.github.io/cookiecutter-data-science/
[homebrew]: https://brew.sh/
[issue-windows-os]: https://github.com/ukgovdatascience/govcookiecutter/issues/20
[pluralsight]: https://www.pluralsight.com/tech-blog/managing-python-environments/
[pre-commit]: https://pre-commit.com/
[youtube]: https://www.youtube.com/watch?v=N7_d3k3uQ_M
[youtube-creation]: https://youtu.be/N7_d3k3uQ_M?t=907
