# `govcookiecutter`

A cookiecutter template for analytical, Python-, or Python and R-based projects within
Her Majesty's Government, and wider public sector.

This template helps to set up standardised project structures, and [includes security
features using pre-commit hooks][docs-pre-commit].

It also provides an Agile, centralised, and lightweight analytical quality assurance
(AQA) process. Pull or merge request templates are used to nudge users to complete this
process. [This helps meet HM Government best practice on producing quality analysis, as
defined in the Aqua Book][aqua-book].

[For reasons why we developed `govcookiecutter`, read the blog post][blog-post], and
[watch the live demonstration from March 2021 on version 0.5.3][youtube].

## Getting started

[First, make sure your system meets the
requirements](#requirements-to-create-a-cookiecutter-template). Next, open your
terminal, navigate to the directory where you want your new repository to exist. Then
run the following command for the latest stable release:

```shell
cookiecutter https://github.com/best-practice-and-impact/govcookiecutter.git
```

or for a specific branch, tag, or commit SHA `{SPECIFIC}`, run:

```shell
cookiecutter https://github.com/best-practice-and-impact/govcookiecutter.git --checkout {SPECIFIC}
```

Follow the prompts; if you are asked to re-download `govcookiecutter`, input `yes`.
Default responses are shown in the squared brackets; to use them, leave your response
blank, and press enter.

Once you've answered all the prompts, your project will be created. Then:

1. Set up a Python virtual environment — [there are many ways to set up a virtual
  environment][pluralsight], so we'll let you decide what's best for you!
2. In your terminal, navigate to your new project, and initialise Git
   ```shell
   git init
   ```
3. Install the necessary packages using `pip` and the pre-commit hooks:
   ```shell
   pip install -r requirements.txt
   pre-commit install
   ```
   or use the `make` command:
   ```shell
   make requirements
   ```
4. Stage all your project files, and make your first commit
   ```shell
   git add .
   git commit -m "Initial commit"
   ```

Once you've completed these steps, [consider making some optional changes before
kicking off your project development](#optional-changes-to-consider-post-project-creation).

### Requirements to create a cookiecutter template


[```Contributors have some additional requirements!```](https://github.com/best-practice-and-impact/govcookiecutter/blob/main/CONTRIBUTING.md/)


To get started your system should meet the following requirements:

1. Python 3.6.1+ installed
2. R 4.0.4+ installed (optional)[^1]
3. The [`cookiecutter` package installed](#installing-the-cookiecutter-package)

[^1]: Only for combined Python and R projects, if selected in the prompts during
project creation.

#### Installing the `cookiecutter` package

There are many ways to install the `cookiecutter` package. Our recommendation is to
install it at the system or user level, rather than as a Python package with `pip` or
`conda`. This ensures it is isolated from the rest of your system, and always available.

For macOS, open your terminal, and [install `cookiecutter` with Homebrew][homebrew]:

```shell
brew install cookiecutter
```

For Debian/Ubuntu, use the following commands:

```shell
sudo apt-get install cookiecutter
```

Otherwise, you can install `cookiecutter` with `pip` — you may wish to create a virtual
environment first:

```shell
python -m pip install --user cookiecutter
```

## Optional changes to consider post-project creation

Here are some suggested changes to make before your first commit:

- consider [using the `cruft` package to integrate future `govcookiecutter`
  releases][cruft]
  ```shell
  pip install cruft
  cruft link https://github.com/best-practice-and-impact/govcookiecutter
  ```
- make sure the `README.md` reflects what you want to do with your project
- have a look inside the `docs/aqa` folder, as you may want to modify some of this
  analytical quality assurance documentation (AQA), for example the AQA plan
- (if present) confirm that the pull or merge request template checklists meet your
  requirements
  - These can be found at `.github/pull_request_template.md` (GitHub), or in
    `.gitlab/merge_request_templates` folder (GitLab)

## Licence

Unless stated otherwise, the codebase is released under the MIT License. This covers
both the codebase and any sample code in the documentation. The documentation is ©
Crown copyright and available under the terms of the Open Government 3.0 licence.

## Contributing

[If you want to help us build, and improve `govcookiecutter`, view our contributing
guidelines](./CONTRIBUTING).

## Acknowledgements

[This template is based off the DrivenData Cookiecutter Data Science
project][drivendata]. Specifically, it uses similar `data` and `src` folder structures,
and a modified version of the `help` commands in the `Makefile`s.

[aqua-book]: https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government
[blog-post]: https://dataingovernment.blog.gov.uk/2021/07/20/govcookiecutter-a-template-for-data-science-projects/
[cruft]: https://github.com/cruft/cruft
[docs-pre-commit]: ./%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/pre_commit_hooks.md
[drivendata]: http://drivendata.github.io/cookiecutter-data-science/
[homebrew]: https://brew.sh/
[issue-windows-os]: https://github.com/best-practice-and-impact/govcookiecutter/issues/20
[pluralsight]: https://www.pluralsight.com/tech-blog/managing-python-environments/
[youtube]: https://www.youtube.com/watch?v=N7_d3k3uQ_M
[issue20]: https://github.com/best-practice-and-impact/govcookiecutter/issues/20
