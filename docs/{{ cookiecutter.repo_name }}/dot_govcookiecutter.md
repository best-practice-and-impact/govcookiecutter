# `.govcookiecutter` folder overview

## manifest.json

Used in cookiecutter configuation for removing files in the created repository that are not required
for users not using R.

## organisational_frameworks/

Contains folders for organisation-specific frameworks. These allow for customisation of the created repository.
The folders require:

- A template Analytical Quality Assurance (AQA) plan
- A template data log
- A template assumptions and caveats log
- A `pull_request_template.md`
- A `README.md`.

`govcookiecutter` currently contains a Government Digital Service framework.
