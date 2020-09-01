from textwrap import dedent

# Get the user-defined option around whether or not they would like to create a secrets file
require_secrets = "{{ cookiecutter.create_secrets_file }}"

# Check if `require_secrets` is 'Yes'
if require_secrets == "Yes":

    # Define a header for the `.secrets file`
    secrets_file = """
    # Secrets go here, and can be read in by Python using `os.environ.get`:
    #
    #   --------------------------------------------------------
    #   import os
    #
    #   EXAMPLE_SECRET = os.environ.get("EXAMPLE_SECRET")
    #   --------------------------------------------------------
    #
    # This file is NOT version-controlled!

    # Google Cloud authentication credentials
    export GOOGLE_APPLICATION_CREDENTIALS=""
    """

    # Write the `.secrets` file out
    with open(".secrets", "w") as f:
        f.write(dedent(secrets_file).lstrip())
