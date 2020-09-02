from textwrap import dedent


def create_secrets_file(user_option: str) -> None:
    """Create a .secrets file depending on a user option.

    Args:
        user_option (str): User option.

    Returns:
        A .secrets file created in the top-level if user_option is 'Yes', otherwise nothing.

    """

    # Check if `user_option` is 'Yes'
    if user_option == "Yes":

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


if __name__ == "__main__":

    # Create a .secrets file, if requested
    create_secrets_file("{{ cookiecutter.create_secrets_file }}")
