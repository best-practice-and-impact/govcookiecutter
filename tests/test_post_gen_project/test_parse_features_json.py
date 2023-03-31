import json
from collections import Counter
from pathlib import Path
from typing import Dict, List

import pytest

from hooks.post_gen_project import parse_features_json

# Keys for the JSON file
JSON_BASE_KEYS = ["name", "remove", "resources"]


@pytest.fixture
def make_temporary_features_json(
    make_temporary_folders_and_files: Path,
    test_input_json: Dict,
    test_input_json_filename: str,
) -> Path:
    """Make a temporary features JSON file."""

    # Define the list of folders and filenames for possible removal

    # Define the file path for the temporary features JSON file, then write its contents
    temp_json_path = make_temporary_folders_and_files.joinpath(test_input_json_filename)
    temp_json_path.touch()
    with open(temp_json_path, "w", encoding="utf-8") as f:
        json.dump(test_input_json, f)
    return temp_json_path


# Define the test cases for the `TestParseFeaturesJson` test class
args_test_parse_features_json_attributes = [
    (
        ["d"],
        ["e"],
        ["a.txt", "b/c.txt"],
        ["c/f.txt"],
        ["A", True, ["a.txt", "b/c.txt", "d"]],
        "test_manifest.json",
    ),
    (
        ["d"],
        ["e"],
        ["a.txt", "b/c.txt"],
        ["c/f.txt"],
        ["A", False, ["a.txt", "b/c.txt", "d"]],
        "test_manifest.json",
    ),
    (
        ["1", "2"],
        ["3", "4"],
        ["a.txt", "1/b.txt", "2/c/d.txt"],
        ["4/e.txt"],
        ["B", True, ["1", "2", "a.txt", "1/b.txt", "2/c/d.txt"]],
        "example_manifest.json",
    ),
    (
        ["1", "2"],
        ["3", "4"],
        ["a.txt", "1/b.txt", "2/c/d.txt"],
        ["4/e.txt"],
        ["B", False, ["1", "2", "a.txt", "1/b.txt", "2/c/d.txt"]],
        "example_manifest.json",
    ),
]
args_test_parse_features_json = [
    (*a[:4], {"features": [dict(zip(JSON_BASE_KEYS, a[4]))]}, a[5])
    for a in args_test_parse_features_json_attributes
]


@pytest.mark.parametrize(
    "test_input_folder_names, test_extra_folder_names, test_input_filenames, "
    "test_extra_filenames, test_input_json, test_input_json_filename",
    args_test_parse_features_json,
)
class TestParseFeaturesJson:
    def test_json_load_called_correctly(
        self, mocker, make_temporary_features_json: Path
    ) -> None:
        """Test that ``json.load`` is called correctly."""

        # Patch both `builtins.open`, and `json.load`
        patch_open = mocker.patch("builtins.open", mocker.mock_open(read_data="data"))
        patch_json_load = mocker.patch("hooks.post_gen_project.load")

        # Execute the function, and check the patches are called appropriately
        _ = parse_features_json(make_temporary_features_json)
        patch_open.assert_called_once_with(
            make_temporary_features_json, encoding="utf-8"
        )
        patch_json_load.assert_called_once_with(patch_open())

    def test_returns_correctly(
        self,
        make_temporary_features_json: Path,
        test_input_folder_names: List[str],
        test_input_filenames: List[str],
        test_input_json: Dict,
    ) -> None:
        """Test that the function returns as expected."""

        # Generate the expected outputs, execute the function, and test it return as
        # expected, if the `remove` key is True
        if test_input_json["features"][0]["remove"]:
            test_expected = [
                Path(p).resolve()
                for p in [*test_input_folder_names, *test_input_filenames]
            ]
            test_output = parse_features_json(make_temporary_features_json)
            assert Counter(test_output) == Counter(test_expected)
        else:
            assert parse_features_json(make_temporary_features_json) == []
