# Modifying `govcookiecutter`

```{warning}
It's strongly recommended you build an example project to test that your changes work!
```

[`govcookiecutter` uses the `cookiecutter` Python package][cookiecutter] to build
template project structures. In turn, [`cookiecutter` uses Jinja templating to inject
user-defined variables][jinja] into files, file names, and folder names. Most of these
variables are based on answers to prompts when you run the `cookiecutter` command.

## `cookiecutter` template generation

When you open your terminal and run:

```shell
cookiecutter https://github.com/best-practice-and-impact/govcookiecutter.git
```

you'll see a list of prompts to answer; one of them is `repo_name`.

Your answer for `repo_name` is used to overwrite every instance of
`{{ cookiecutter.repo_name }}`. The first instance is the `govcookiecutter` folder
`{{ cookiecutter.repo_name }}`, which becomes your outputted project!

This means every folder and file contained within the `{{ cookiecutter.repo_name }}`
folder becomes part of your output project, including their content. Anything else
outside of this folder in `govcookiecutter` will not exist in the outputted project.

### Understanding `cookiecutter.json`

The prompts, and their default responses are defined in `cookiecutter.json`. Here, any
keys starting with `_` are not shown to the user, but provide template extensions.

One such extension is `jinja2_time.TimeExtension`, which is used to add the correct
year in the `{{ cookiecutter.repo_name }}/LICENSE` file.

All other keys are used to inject the user responses throughout the template. This
happens wherever you see `{{ cookiecutter.{KEY} }}`, where `{KEY}` is the key in
question.

The values in `cookiecutter.json` are the default responses, shown in squared brackets
to the user. If the user does not enter a response, these default values are used.
Values that are lists are shown as numerical options to the user, with the first list
element as the default value.

Note that these default values can also contain Jinja templating! For example, the
default response for `repo_name` is actually based on `project_name`, but with all
characters in lowercase, and any spaces replaced with hyphens.

## Validating user entries

User entries are validated with pre-generation hooks, which are defined in
`hooks/pre_gen_project.py`. These hooks run before a project is created and, if they
fail, will not create the project.

The only supported validation currently is for a [valid email address, based on the
HTML5 standard for email address format][html5-email-format].

## Conditional files and/or folders

Conditional folders and/or files are items than only exist if actively selected for the
user. For example, if users select `No` for the `using_R` prompt, any R files and
content is removed from their outputted project.

```{note} Folder and file names with Jinja templating

Do not use Jinja templating for conditional folders and/or files, as certain characters
may not be supported on all operating systems.

```

This functionality is provided by post-generation hooks in `govcookiecutter`, which are
defined in `hooks/post_gen_project.py`. These hooks only run after a project has been
generated and, if they fail, will rollback the entire project.

Conditional files and folders are defined as `features` in the
`{{ cookiecutter.repo_name }}/manifest.json` file, which looks like:

```
{
  "features": [
    {
      "name": "A name",
      "description": "A description.",
      "remove": {% if cookiecutter.{KEY} == {VALUE} %}true{% else %}false{% endif %},
      "resources": ["A", "list", "of", "files", "and/or", "folders"]
    }
  ]
}
```

where `{KEY}` and `{VALUE}` are `cookiecutter.json` keys and values.

This works by using Jinja conditional templating to either set the `remove` value to
true or false. The post-generation hook then scans through this JSON file deleting all
files and folders listed in the `resources` value where `remove == true`.

### Changing conditional folders and files

If an existing feature has a `remove` condition that meets your needs, amend its
`resources` list to change the folders/files that will be removed.

To add a new feature, add a dictionary within the `features` list, which has at least
the `remove` and `resources` keys. Add your Jinja conditional for the `remove` value,
and a list of files/folders for the `resources` key. For documentation purposes, it's
good practice to add `name` and `description` keys as well!

To remove a feature, delete the appropriate dictionary from the `features` list.

## Conditional file content

Jinja conditional statements can be used display content based on the user responses.
For example, for the following Markdown:

```markdown
### `CONTRIBUTING.md`

The contributing guidelines for this project.

{% if cookiecutter.using_R == "Yes" -%}
### `DESCRIPTION`

R-specific information related to the project including the name, authors and packages
necessary for the project.

{% endif -%}

### `LICENSE`

The licence for this project...
```

the `DESCRIPTION` section is conditional on the user response to the `using_R` prompt.

Notice the hyphen before the trailing `%` in each Jinja statement; this hyphen controls
blank space after the statement. A hyphen after the leading `%` in a Jinja statement
controls blank space before the element.

## Replacing folders and files

[Replacing folders and files a more involved change, and is currently supported for
AQA frameworks and pull/merge request templates only][docs-organisational-frameworks].
These are performed in the `hooks/post_gen_project.py`file.

## Tests, coverage, and continuous integration

All pre- and post-generation hooks should be fully tested, alongside any generic
functions that we want to supply to users within the `{{ cookiecutter.repo_name }}`
package. These tests should be written in `tests` or
`{{ cookiecutter.repo_name }}/tests` as appropriate.

Coverage also only covers the `hooks` and `{{ cookiecutter.repo_name }}/{{ cookiecutter.repo_name.lower().replace(' ', '_').replace('-', '_') }}` folders.

### Testing Jinja templating

Most of the tests are straightforward, and comprehensive. However, to test the Jinja
injection of user responses, the `test_govcookiecutter_injected_variables.py` script
adopts a test-driven development approach to completeness.

This test parses all the content of the `{{ cookiecutter.repo_name }}` folder, and
counts the number of times the replacement variable and its variations appear.

The constant dictionary variables at the top of the test script define the different
variations of Jinja templating expected for each prompt, and their expected counts.
The dictionary keys are replaced during the test with the test input variables.

If you modify the content, beware that these counts may change, so you will have to
change these counts to pass the tests.

### Continuous integration

Continuous integration (CI) is provided by GitHub Actions. For all pushes to the
repository, GitHub Actions will:

- install the requirements
- run pre-commit hooks on all files
- create the documentation to check for errors and warnings
  - only errors are checked for Windows
- check for broken external links in the documentation
- run tests and coverage
- upload coverage reports to CodeCov

These "on push" CI checks are run on Ubuntu, macOS, and Windows operating systems, as
well as Python 3.6+. This Action can be found at `workflows/govcookiecutter-build.yml`.

When a pull request is raised, GitHub Actions will also:

- build an example project
- navigate into the example project
- initialise Git
- install requirements
- build the example project documentation, checking for errors but not warnings
- check for broken external links in the documentation
- run pre-commit hooks on all files

These "on pull request" CI checks are run on Ubuntu, and macOS operating systems, as
well as Python 3.6+, and for example projects with or without R 4.0.4+.

[To understand why only certain operating systems are supported for GitHub Actions,
see GitHub issues 29 and 30][github-issues].

## Releases

Pull requests are raised on GitHub, and approved features are merged into `main`. [We
then use semantic versioning to number our releases][semver]. This helps our users
select a different version of `govcookiecutter` to use based on their individual needs.

[cookiecutter]: https://cookiecutter.readthedocs.io
[docs-organisational-frameworks]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/docs/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.govcookiecutter/organisational_frameworks/docs_repo_frameworks_README.md
[github-issues]: https://github.com/best-practice-and-impact/govcookiecutter/issues
[html5-email-format]: https://html.spec.whatwg.org/multipage/input.html#valid-e-mail-address
[jinja]: https://jinja.palletsprojects.com
[semver]: https://semver.org/
