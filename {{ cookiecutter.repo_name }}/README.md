# `{{ cookiecutter.project_name }}`

{{ cookiecutter.overview }}

> ℹ️ Where this documentation refers to the **root folder** we mean where this README.md is located.

- [Getting started](#getting-started)
  - [Requirements](#requirements)
{% if cookiecutter.create_secrets_file == "Yes" %}- [Required secrets and credentials](#required-secrets-and-credentials){% endif -%}
- [Licence](#licence)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## Getting started

To be added.

### Requirements

{% if cookiecutter.create_secrets_file == "Yes" %}- A `.secrets` file with the [required secrets and credentials](#required-secrets-and-credentials){% endif -%}
- [Load environment variables][docs-loading-environment-variables] from `.envrc`

To be added.
{% if cookiecutter.create_secrets_file == "Yes" %}
## Required secrets and credentials

To run this project, first make sure [you have a `.secrets` file][docs-loading-environment-variables-secrets]. Then,
add the following lines to it to load secrets and credentials as environment variables:

```shell
export SOME_VARIABLE=SOME_VALUE
```

Once you've made this change you will need to [load these variables via `.envrc`][docs-loading-environment-variables].
{% endif -%}
## Licence

Unless stated otherwise, the codebase is released under the MIT License. This covers both the codebase and any sample
code in the documentation. The documentation is © Crown copyright and available under the terms of the Open Government
3.0 licence.

## Contributing

If you want to help us build, and improve `{{ cookiecutter.project_name }}`, view our
[contributing guidelines][contributing].

## Acknowledgements

This project structure is based on the `govcookiecutter` template project.

[contributing]: ./CONTRIBUTING.md
[govcookiecutter]: https://github.com/ukgovdatascience/govcookiecutter
[docs-loading-environment-variables]: ./docs/user_guide/loading_environment_variables.md
[docs-loading-environment-variables-secrets]: ./docs/user_guide/loading_environment_variables.md#storing-secrets-and-credentials
[pre-commit]: https://pre-commit.com/
