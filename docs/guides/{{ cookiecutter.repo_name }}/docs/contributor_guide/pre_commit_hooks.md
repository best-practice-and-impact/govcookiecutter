```{include} ../../../../../{{ cookiecutter.repo_name }}/docs/contributor_guide/pre_commit_hooks.md
```

## Pre-commit hooks in the `{{ cookiecutter.repo_name }}` folder

If you are adding or modifying pre-commit hooks, please note that the pre-commit hooks
in the `{{ cookiecutter.repo_name }}` template folder can be different to those at the
top-level of the repository, especially around which folders are inspected.

If you wish to add or modify pre-commit hooks in the `.pre-commit-config.yaml` file in
the template folder, it's strongly recommended that you build an example repository,
and test out your changes.
