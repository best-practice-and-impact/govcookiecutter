# `hooks` API reference

This page gives an overview of all public `hooks` objects, functions and methods. All
classes and functions exposed in `hooks.*` namespace are public.

<!-- Functions should be referenced in the `hooks.__init__.py` -->
```{eval-rst}
.. currentmodule:: hooks
```

## Cookiecutter pre-generation hooks

These are functions executed after user input, but before project generation. If any
pre-generation hooks fail, the project will not be generated.

### Prompt input validation

```{eval-rst}
.. autosummary::
    :toctree: api/

    check_valid_email_address_format

```
## Cookiecutter post-generation hooks

These are functions executed after initial project generation by the `cookiecutter`
package. These include moving the selected organisational frameworks to the correct
location, as well as deleting unnecessary files and folders. If any post-generation
hooks fail, the generated project will be rolled-back, and deleted.

### Public sector organisational framework functions

```{eval-rst}
.. autosummary::
    :toctree: api/

    set_aqa_framework
    set_request_template

```

### Post-generation clean up

```{eval-rst}
.. autosummary::
    :toctree: api/

    delete_files_and_folders
    parse_features_json

```
