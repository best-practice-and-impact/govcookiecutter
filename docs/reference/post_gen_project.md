# Post-cookiecutter generation hooks

These `hooks` package functions are executed after the project structure has been generated.

<!-- Functions should be referenced in the `hooks.__init__.py` -->
```{eval-rst}
.. currentmodule:: hooks
```

## Public sector organisational framework functions

```{eval-rst}
.. autosummary::
    :toctree: api/

    set_aqa_framework
    set_request_template

```

## Post-generation clean up

```{eval-rst}
.. autosummary::
    :toctree: api/

    delete_files_and_folders
    parse_features_json

```
