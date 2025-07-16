from json import load
from pathlib import Path
from shutil import rmtree
from typing import List, Union


def delete_files_and_folders(paths: Union[Path, str, List[Path], List[str]]) -> None:
    """Delete files and folders for given file and/or folder paths.

    Args:
        paths: A ``pathlib.Path`` object or string, or list of ``pathlib.Path`` or
        strings.

    Returns:
        None - deletes the files and/or folders defined in ``paths`` if they exist. If
        this function raises an error, the files and/or folders have not been removed.

    """

    # Coerce `paths` into a list of `pathlib.Path` objects. Then remove each folder and
    # file
    paths = [Path(p) for p in paths] if isinstance(paths, List) else [Path(paths)]
    _ = [rmtree(d) for d in paths if d.is_dir() and d.exists()]
    _ = [f.unlink() for f in paths if f.is_file() and f.exists()]


def set_aqa_framework(
    dir_organisational_framework_aqa: Union[Path, str],
    dir_cookiecutter_docs_aqa: Union[Path, str],
) -> None:
    """Set a specific organisational analytical quality assurance (AQA) framework.

    Args:
        dir_organisational_framework_aqa: A folder path that contains a specific
            organisational AQA framework.
        dir_cookiecutter_docs_aqa: A folder path within the outputted project
            structure, where the contents of `dir_organisational_framework_aqa` will
            reside.

    Returns:
        The organisation-specific AQA framework in the outputted project structure's
        `dir_cookiecutter_docs_aqa` folder.

    """

    # Remove the default `docs/aqa` folder, and its contents
    delete_files_and_folders(dir_cookiecutter_docs_aqa)

    # Copy the relevant organisational AQA framework to the `docs/aqa` folder
    _ = Path(dir_organisational_framework_aqa).rename(dir_cookiecutter_docs_aqa)


def parse_features_json(file: Union[Path, str]) -> List[Path]:
    """Parse a JSON file containing filepaths.

    Args:
        file: A filepath to a JSON file containing a ``features`` field, which contains
            a list of dictionaries, where each dictionary must have at least an
            ``remove`` and a `resources` field.

    Returns:
        A list of file paths from the ``resources`` field, if the ``remove`` field is
        True.

    """

    # Load the JSON file, extract the nested `resources` field from the loaded JSON
    # file, if the `enabled` is True.
    # Coerce to a list, then return the list of paths
    with open(file, encoding="utf-8") as json_file:
        d = load(json_file)
    resources = [
        f["resources"] if isinstance(f["resources"], list) else [f["resources"]]
        for f in d["features"]
        if f["remove"]
    ]
    return [Path(e).resolve() for r in resources for e in r]


if __name__ == "__main__":

    # Define the folder path to `.govcookiecutter`
    DIR_GOVCOOKIECUTTER = Path(".govcookiecutter")

    # Check `{{ cookiecutter.organisational_framework }}` is not `N/A`
    if "{{ cookiecutter.organisational_framework }}" != "N/A":

        # Define the folder path to the specific organisation framework of interest in
        # the `organisational_frameworks`
        # folder
        DIR_ORGANISATIONAL_FRAMEWORKS = DIR_GOVCOOKIECUTTER.joinpath(
            "organisational_frameworks", "{{ cookiecutter.organisational_framework }}"
        )

        # Transfer the `aqa` folder, and the pull/merge request templates to the
        # correct folder paths
        set_aqa_framework(
            DIR_ORGANISATIONAL_FRAMEWORKS.joinpath("aqa"), Path("docs").joinpath("aqa")
        )

    # Remove `DIR_GOVCOOKIECUTTER`
    delete_files_and_folders(DIR_GOVCOOKIECUTTER)
