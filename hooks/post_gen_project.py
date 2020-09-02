from shutil import rmtree
from textwrap import dedent
import os

# Define the folder path to the 'docs/aqa_frameworks' folder, and the future `docs/aqa` folder
PATH_DOCS_AQA_FRAMEWORKS = os.path.join("docs", "aqa_frameworks")
PATH_DOCS_AQA = os.path.join("docs", "aqa")


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


def select_dept_aqa_framework(user_option: str, default_option: str = "GDS") -> None:
    """Create analytical quality assurance (AQA) documents for a specific HM Government department.

    Args:
        user_option (str): User option that defines a HM Government departmental AQA framework to use
        default_option (str): Default: GDS. Default option if user_option is not an existing framework.

    Returns:
        A new folder in docs/aqa containing the selected HM Government departmental AQA framework.

    """

    # Get all the directories in `PATH_DOCS_AQA_FRAMEWORKS`
    all_folders = [d for d in os.listdir(PATH_DOCS_AQA_FRAMEWORKS) if os.path.isdir(d)]

    # Select the correct folder; use `default_option` if `user_option` is not a valid sub-folder in `all_folders`
    selected_folder = user_option if user_option in all_folders else default_option

    # Copy the relevant HM Government departmental AQA framework to the `docs/aqa` folder, using `default_option` if
    # `user_option` is not a valid sub-folder in `PATH_DOCS_AQA_FRAMEWORKS`
    os.rename(os.path.join(PATH_DOCS_AQA_FRAMEWORKS, selected_folder), PATH_DOCS_AQA)

    # Remove all framework folders now we have the correct AQA framework
    rmtree(PATH_DOCS_AQA_FRAMEWORKS)


if __name__ == "__main__":

    # Create a .secrets file, if requested
    create_secrets_file("{{ cookiecutter.create_secrets_file }}")

    # Select the appropriate AQA framework
    select_dept_aqa_framework("{{ cookiecutter.departmental_aqa_framework }}")
