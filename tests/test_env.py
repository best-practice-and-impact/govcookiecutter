from pathlib import Path
from typing import Dict, List

from dotenv import dotenv_values

# Define a path to the `govcookiecutter` template directory, and its `.env` file
DIR_TEMPLATE = Path("{{ cookiecutter.repo_name }}")
PATH_TEMPLATE_ENV = DIR_TEMPLATE.joinpath(".env")

# Define a list of directory names to recursively ignore, as well as a list of
# directory names to ignore at the root-level of the `govcookiecutter` template
# directory, and a list of dictionary names to ignore in certain root-level directories
EXCLUDE_DIR_NAMES = ["__pycache__", "example_modules"]
EXCLUDE_ROOT_DIR_NAMES = [*EXCLUDE_DIR_NAMES, ".govcookiecutter"]
EXCLUDE_SUB_DIR_IN_PARENTS_NAMES = [*EXCLUDE_ROOT_DIR_NAMES, "docs"]


def remove_brackets_and_spaces(path_name: str) -> str:
    """Removes spaces and brackets from a string.

    Args:
        path_name : A path name as a string.

    Returns:
        The path name with spaces and brackets removed.
    """
    if "{" in path_name or "}" in path_name or " " in path_name:
        path_name = path_name.replace("{", "")
        path_name = path_name.replace("}", "")
        path_name = path_name.replace(" ", "")

    return path_name


def loop_directories_children(
    dir: Path, env_expected_dir_variable: Dict[str, Path]
) -> Dict[str, Path]:
    """Loop through a directories children and add their paths to a dictionary.

    Args:
        dir: directory containing Children locations
        env_expected_dir_variable : Dictionary where the keys are directory
            variables and values are their paths.

    Returns:
        Dictionary of directory keys and their paths with the children of the
        given directory added.
    """
    for child in dir.iterdir():
        if child.is_dir():
            dir_name = remove_brackets_and_spaces(dir.name.upper())
            child_name = remove_brackets_and_spaces(child.name.upper())
            env_expected_dir_variable[f"DIR_{dir_name}_{child_name}"] = child
    return env_expected_dir_variable


def get_actual_env_variables(path_env: Path) -> Dict[str, Path]:
    """Get the environment variables and values for directories in the `.env` file of
     the `govcookiecutter` template.

    Args:
        path_env: A file path to the `.env` file of the `govcookiecutter` template.

    Returns:
        A dictionary where the keys are the names of the directory variables, and the
        values are the directory paths.

    """
    directory_variables = {}
    for variable, value in dotenv_values(path_env).items():
        if variable.startswith("DIR_"):
            path_value = path_env.parent.joinpath(value).resolve()
            directory_variables[variable] = path_value.relative_to(Path.cwd())
    return directory_variables


def define_expected_env_variables(
    folder: Path,
    exclude_folders: List[str],
    exclude_root_folders: List[str],
    exclude_sub_folders_in_parent_folders: List[str],
) -> Dict[str, Path]:
    """Get the expected directory variables and values in the `.env` file of the
    `govcookiecutter` template.

    Args:
        folder: A folder path to the `govcookiecutter` template folder.
        exclude_folders: A list of folder names to ignore when encountered.
        exclude_root_folders: A list of root-level folder names in `folder` to ignore.
        exclude_sub_folders_in_parent_folders: A list of folder names at the root-level
            of `folder` where their sub-folders should be ignored.

    Returns:
        A dictionary where the keys are expected directory variables, and the values
        are the expected directory paths of the `.env` file in the `govcookiecutter`
        template directory `folder`.

    """

    # Get the names of all root-level directories in `folder`, where each name is in
    # upper case in the format "DIR_<<<DIRECTORY_NAME>>>". Ignore any directories
    # with a name in `exclude_root_folders`
    env_expected_dir_variable = {
        f"DIR_{remove_brackets_and_spaces(d.name.upper())}": d
        for d in folder.glob("*")
        if d.is_dir() and d.name not in exclude_root_folders
    }

    # Get all sub-directory names one-level down from `folder`, where the directory
    # name is not in `exclude_folders`, and the parent directory name is not in
    # `exclude_sub_folders_in_parent_folders`. Each name is in upper case in the
    # format "DIR_<<<PARENT_DIRECTORY_NAME>>>_<<<DIRECTORY_NAME>>>". Return
    # `env_expected_dir_variable`
    for d in folder.glob("*/*"):
        if (
            d.is_dir()
            and d.name not in exclude_folders
            and d.parent.name not in exclude_sub_folders_in_parent_folders
        ):
            if (
                d.name.upper()
                == "{{ cookiecutter.repo_name.lower().replace(' ', '_').replace('-', '_') }}".upper()  # noqa: E501
            ):
                env_expected_dir_variable = loop_directories_children(
                    d, env_expected_dir_variable
                )

            parent = remove_brackets_and_spaces(d.parent.name.upper())
            name = remove_brackets_and_spaces(d.name.upper())
            env_expected_dir_variable[f"DIR_{parent}_{name}"] = d
    return env_expected_dir_variable


class TestEnvExportDirectories:
    def test_values_are_directories(self) -> None:
        """Test that the values are real directories."""
        for n, d in get_actual_env_variables(PATH_TEMPLATE_ENV).items():
            assert d.is_dir(), f"{repr(n)} variable directory does not exist: {d}"

    def test_variables_as_expected(self) -> None:
        """Test directory variable and value names in `.env` are as expected."""

        # Get the expected `.env` directory variables, and assert the actual
        # variables are as expected
        test_expected = define_expected_env_variables(
            DIR_TEMPLATE,
            EXCLUDE_DIR_NAMES,
            EXCLUDE_ROOT_DIR_NAMES,
            EXCLUDE_SUB_DIR_IN_PARENTS_NAMES,
        )
        assert get_actual_env_variables(PATH_TEMPLATE_ENV) == test_expected
