from pathlib import Path
from typing import List
from unittest.mock import MagicMock, call

import pytest

from hooks.post_gen_project import delete_files_and_folders


@pytest.fixture
def patch_rmtree(mocker) -> MagicMock:
    """Patch the ``rmtree`` function."""
    return mocker.patch("hooks.post_gen_project.rmtree")


@pytest.fixture
def patch_path(mocker) -> MagicMock:
    """Patch the ``pathlib.Path`` function."""
    return mocker.patch("hooks.post_gen_project.Path", side_effect=Path)


@pytest.fixture
def patch_path_unlink(mocker) -> MagicMock:
    """Patch the ``pathlib.Path.unlink`` function."""
    return mocker.patch("hooks.post_gen_project.Path.unlink")


# Define test cases for the `TestDeleteFilesAndFolders` test class
args_test_delete_files_and_folders = [
    (["a"], ["b"], [], []),
    ([], [], ["hello.txt"], ["world.md"]),
    (
        ["a", "b", "c"],
        ["1", "2", "3"],
        ["hello.txt", "a/world.txt", "b/d/foo.txt", "c/e/f/bar.txt"],
        ["3/a.txt", ".b"],
    ),
    (
        ["1", "2", "3"],
        ["a", "b", "c"],
        ["hello.md", "1/a/b/world.py", "2/foo.R", "3/bar.json"],
        ["hello_world.txt"],
    ),
]


@pytest.mark.parametrize(
    "test_input_folder_names, test_extra_folder_names, test_input_filenames, "
    "test_extra_filenames",
    args_test_delete_files_and_folders,
)
class TestDeleteFilesAndFolders:
    def test_path_unlink_called_correctly(
        self,
        patch_path: MagicMock,
        patch_path_unlink: MagicMock,
        make_temporary_folders_and_files: Path,
        test_input_folder_names: List[str],
        test_input_filenames: List[str],
    ) -> None:
        """Test ``pathlib.Path.unlink`` is called the correctly."""

        # Define the input list of folders, and file paths
        test_input_folder_names = [
            make_temporary_folders_and_files.joinpath(d)
            for d in test_input_folder_names
        ]
        test_input_filenames = [
            make_temporary_folders_and_files.joinpath(f) for f in test_input_filenames
        ]
        test_input = [*test_input_folder_names, *test_input_filenames]

        # Assert everything exists, and then execute the function
        assert all([p.exists() for p in test_input])
        delete_files_and_folders(test_input)

        # Assert `pathlib.Path` has been called correctly for all folder and file
        # names, and that `pathlib.Path.unlink` has been called the correct number of
        # times
        patch_path.assert_has_calls([call(p) for p in test_input])

        # Assert that `pathlib.Path.unlink` has removed the filenames
        assert all([not f.exists() for f in test_input_filenames])

    def test_rmtree_called_correctly(
        self,
        patch_rmtree: MagicMock,
        make_temporary_folders_and_files: Path,
        test_input_folder_names: List[str],
        test_input_filenames: List[str],
    ) -> None:
        """Test the `rmtree` function is called correctly."""

        # Define the input list of folders, and file paths
        test_input_folder_names = [
            make_temporary_folders_and_files.joinpath(d)
            for d in test_input_folder_names
        ]
        test_input_filenames = [
            make_temporary_folders_and_files.joinpath(f) for f in test_input_filenames
        ]
        test_input = [*test_input_folder_names, *test_input_filenames]

        # Assert everything exists, execute the function, and check `rmtree` is called
        # correctly
        assert all([p.exists() for p in test_input])
        delete_files_and_folders(test_input)
        patch_rmtree.assert_has_calls([call(d) for d in test_input_folder_names])

    def test_operates_correctly(
        self,
        make_temporary_folders_and_files: Path,
        test_input_folder_names: List[str],
        test_extra_folder_names: List[str],
        test_input_filenames: List[str],
        test_extra_filenames: List[str],
    ) -> None:
        """Test the function operates correctly, and removes all files and folders."""

        # Define the input list of folders, and file paths
        test_input = [
            make_temporary_folders_and_files.joinpath(p)
            for p in [*test_input_folder_names, *test_input_filenames]
        ]

        # Define the extra folders and files that should not be deleted
        test_extra = [
            make_temporary_folders_and_files.joinpath(p)
            for p in [*test_extra_folder_names, *test_extra_filenames]
        ]

        # Assert everything exists, and execute the function
        assert all([p.exists() for p in [*test_input, *test_extra]])
        delete_files_and_folders(test_input)

        # Assert that only the paths defined in `test_input` have been removed
        assert all([p.exists() for p in test_extra])
        assert all([not p.exists() for p in test_input])
