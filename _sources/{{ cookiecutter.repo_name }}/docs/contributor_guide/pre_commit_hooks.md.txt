```{include} ../../../../{{ cookiecutter.repo_name }}/docs/contributor_guide/pre_commit_hooks.md
```

## Pre-commit hooks in the `{{ cookiecutter.repo_name }}` folder

If you're changing any pre-commit hooks, note that `.pre-commit-config.yaml` can be
different to `{{ cookiecutter.repo_name }}/.pre-commit-config.yaml`. This includes
which pre-commit hooks are run, as well as on which folders.

It's strongly recommended that you build an example project to test out your changes.
