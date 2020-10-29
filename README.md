# `govcookiecutter`

A cookiecutter template for analytical, code-based projects within Her Majesty's Government.

- [Who/what is this for?](#whowhat-is-this-for)
- [Getting started](#getting-started)
  - [Requirements](#requirements)
- [Things to consider changing post-creation](#things-to-consider-changing-post-creation)
- [Licence](#licence)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## Who/what is this for?

This template is for any HM Government analyst(s) who codes! It's main purpose is to:

1. Provide a lightweight, Agile-like approach to Analytical Quality Assurance (AQA)
2. Help quickly set up standardised project structures.

For more information about AQA, see [The Aqua Book][aqua-book], and its [resources][aqua-book-resources].

Rather than using different files and locations to store AQA and documentation, our intention is to centralise as much
of this as possible onto your Git repository hosting platform, e.g. GitHub or GitLab.

We use nudges, such as checklists in pull/merge requests, to minimise the burden on contributors and reviewers to
complete AQA checks. This results in faster iterative development and deployment, whilst ensuring HM Government-wide
standards on assurance are met.

We have also included [pre-commit hooks][pre-commit] to prevent accidental committing of secrets, large data files, and
Jupyter notebook outputs for security purposes.

## Getting started

> ⚠️ Only Unix-based systems (macOS, Linux, ...), and Python projects for GitHub or GitLab are supported — feel free to
> [contribute](#contributing) to support other operating systems/programming languages!

To use this template to start your next coding project, make sure your system meets the [requirements](#requirements).

Once you're all set up, open your terminal, navigate to the directory where you want your new repository to exist, and
run the following commands:

```shell script
pip install cookiecutter
cookiecutter https://github.com/ukgovdatascience/govcookiecutter
```

Follow the prompts, and that's it, you're good to go — happy coding!

There are a few optional things you should consider doing in your new project, and we've detailed them
[here](#things-to-consider-changing-post-creation).

### Requirements

> ℹ️ Contributors have some additional requirements! Check out the [contributing guidelines][contributing] for further
> details.

To get started your system should meet the following requirements:

1. Unix-based system (macOS, Linux, ...)
2. Python 3.5+ installed
3. \[Recommended\] A Python virtual environment set up and activated

There are **many** ways to set up a virtual environment, so we'll let you decide what's best for you!

## Things to consider changing post-creation

Here's a few things you should consider changing once you've created your new project:

- Git is not set up by default — open your terminal, navigate to your new project, run `git init` to set it up
- Make sure the `README.md` reflects what **you** want to do with your project!
- Have a look inside the `docs/aqa` folder; you may want to modify some of them, e.g. the AQA plan
- Want to add some project-specific checklists to the pull/merge request template? See the relevant Markdown files
  within the `.github` (GitHub) or `.gitlab/merge_request_templates` (GitLab) folder

## Licence

Unless stated otherwise, the codebase is released under the MIT License. This covers both the codebase and any sample
code in the documentation. The documentation is © Crown copyright and available under the terms of the Open Government
3.0 licence.

## Contributing

If you want to help us build, and improve `govcookiecutter`, view our [contributing guidelines][contributing].

## Acknowledgements

This template is based off the [DrivenData Cookiecutter Data Science][drivendata] project, especially around the
template data and src folder structures, and the `make help` commands in the Makefiles.

[aqua-book]: https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government
[aqua-book-resources]: https://www.gov.uk/government/collections/aqua-book-resources
[contributing]: ./CONTRIBUTING.md
[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[drivendata]: http://drivendata.github.io/cookiecutter-data-science/
[pre-commit]: https://pre-commit.com/
