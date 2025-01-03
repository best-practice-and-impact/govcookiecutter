from pathlib import Path
from typing import List

import pytest


@pytest.fixture
def temporary_frameworks(
    tmp_path,
    test_input_request_template: str,
    test_input_aqa: str,
) -> Path:
    """Create a temporary frameworks folder with sub-folders, and files."""

    # Create a temporary folder
    dir_example = tmp_path.joinpath("example")

    # Create a temporary frameworks folder, and add an `aqa` folder
    dir_framework = dir_example.joinpath("test_framework")
    dir_framework.joinpath("aqa").mkdir(parents=True)

    # Add text Markdown files in `dir_framework`, and its `aqa` folder
    dir_framework.joinpath("request_template.md").write_text(
        test_input_request_template
    )
    dir_framework.joinpath("aqa", "aqa.md").write_text(test_input_aqa)

    # Return the path to the temporary frameworks folder
    return dir_framework


@pytest.fixture
def make_temporary_folders_and_files(
    tmp_path,
    test_input_folder_names: List[str],
    test_extra_folder_names: List[str],
    test_input_filenames: List[str],
    test_extra_filenames: List[str],
) -> Path:
    """Make temporary folders and files."""

    # Create a temporary parent directory where all these temporary folders, and files
    # will be stored
    folder_parent = tmp_path.joinpath("temporary_dir")

    # Compile the folder and file names together
    test_folder_names = [*test_input_folder_names, *test_extra_folder_names]
    test_filenames = [*test_input_filenames, *test_extra_filenames]

    # Create all the temporary folders and files requested
    _ = [
        folder_parent.joinpath(d).mkdir(parents=True, exist_ok=True)
        for d in test_folder_names
    ]
    for f in test_filenames:
        file_path = folder_parent.joinpath(f)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.touch()
    return folder_parent
