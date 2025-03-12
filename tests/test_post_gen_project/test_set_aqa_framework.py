from pathlib import Path
from unittest.mock import MagicMock

import pytest

from hooks.post_gen_project import delete_files_and_folders, set_aqa_framework


@pytest.fixture
def patch_delete_files_and_folders(mocker) -> MagicMock:
    """Patch the ``delete_files_and_folders`` function."""
    return mocker.patch(
        "hooks.post_gen_project.delete_files_and_folders",
        side_effect=delete_files_and_folders,
    )


# Define test cases for the `TestSetAqaFramework` test class
args_test_set_aqa_framework = ["hello", "world"]
args_test_set_aqa_framework_temporary_frameworks = [
    ("This is the request template.", "This is the AQA file."),
    ("Here is the request template.", "Here is the AQA file."),
]


@pytest.mark.parametrize(
    "test_input_dir_cookiecutter_docs_aqa", args_test_set_aqa_framework
)
@pytest.mark.parametrize(
    "test_input_request_template, test_input_aqa",
    args_test_set_aqa_framework_temporary_frameworks,
)
class TestSetAqaFramework:
    def test_delete_files_and_folders_called_once_correctly(
        self,
        temporary_frameworks: Path,
        patch_delete_files_and_folders: MagicMock,
        test_input_dir_cookiecutter_docs_aqa: str,
    ) -> None:
        """Test the ``delete_files_and_folders`` function is called once correctly."""

        # Define a path to the example output folder, which is the parent of
        # `temporary_frameworks`, and create a directory with an example text file
        dir_docs_aqa = temporary_frameworks.parent.joinpath(
            test_input_dir_cookiecutter_docs_aqa
        )
        dir_docs_aqa.mkdir()
        dir_docs_aqa.joinpath("example.txt").write_text(
            f"New file in: {repr(test_input_dir_cookiecutter_docs_aqa)}"
        )

        # Execute the `set_aqa_framework` function
        set_aqa_framework(temporary_frameworks, dir_docs_aqa)

        # Assert `delete_files_and_folders` is called once correctly, then delete the
        # output folder for the next test
        # execution
        patch_delete_files_and_folders.assert_called_once_with(dir_docs_aqa)

    def test_aqa_framework_folder_moved_correctly(
        self,
        temporary_frameworks: Path,
        test_input_request_template: str,
        test_input_aqa: str,
        test_input_dir_cookiecutter_docs_aqa: str,
    ) -> None:
        """Test the right AQA framework folder is moved to the correct location."""

        # Define a path to the example output folder, which is the parent of
        # `temporary_frameworks`, and create a
        # directory with an example text file
        dir_docs_aqa = temporary_frameworks.parent.joinpath(
            test_input_dir_cookiecutter_docs_aqa
        )
        dir_docs_aqa.mkdir()
        dir_docs_aqa.joinpath("example.txt").write_text(
            f"New file in: {repr(test_input_dir_cookiecutter_docs_aqa)}"
        )

        # Execute the `set_aqa_framework` function
        set_aqa_framework(temporary_frameworks, dir_docs_aqa)

        # Assert the correct text has been written
        assert (
            dir_docs_aqa.joinpath("request_template.md").read_text()
            == test_input_request_template
        )
        assert dir_docs_aqa.joinpath("aqa", "aqa.md").read_text() == test_input_aqa

        # Assert the `dir_framework` has been removed
        assert not temporary_frameworks.exists()
