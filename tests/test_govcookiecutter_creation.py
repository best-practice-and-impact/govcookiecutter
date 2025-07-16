import re
from typing import Dict

import pytest
from sphinx.cmd.build import main


@pytest.mark.skip(
    reason="Unclear how to test this, unless there is a title in each " "framework"
)
def test_organisational_framework_correct() -> None:
    """Test that the correct organisational framework is built."""
    pass


@pytest.mark.parametrize("test_input_repository_name", ["a", "b"])
def test_repo_name_directory_correct(
    cookies,
    test_input_repository_name: str,
) -> None:
    """Check the project repository is generated with the correct name."""

    # Create a new project adding extra context
    test_output_project = cookies.bake(
        extra_context={
            "repo_name": test_input_repository_name,
        }
    )

    # Check that the build passes
    assert test_output_project.exit_code == 0
    assert test_output_project.exception is None

    # Check that the repository name is correct, and it is a directory
    assert test_output_project.project_path.name == test_input_repository_name
    assert test_output_project.project_path.is_dir()


# Define the test cases for the `test_builds_correctly` test
args_builds_correctly = [
    {
        "organisation_name": "org_1",
        "organisation_handle": "handle_1",
        "contact_email": "email@1",
        "project_name": "Project_1",
        "repo_name": "repo_1",
        "project_version": "version_1",
    },
    {
        "organisation_name": "org_2",
        "organisation_handle": "handle_2",
        "contact_email": "email@2",
        "project_name": "Project_2",
        "repo_name": "repo_2",
        "project_version": "version_2",
    },
]


@pytest.mark.parametrize("test_input_context", args_builds_correctly)
@pytest.mark.parametrize("test_input_organisational_framework", ["GDS", "N/A"])
def test_builds_correctly(
    cookies,
    test_input_context: Dict[str, str],
    test_input_organisational_framework: str,
) -> None:
    """Test that the projects are built correctly with no errors."""

    # Create a new project adding extra context
    test_output_project = cookies.bake(
        extra_context={
            **test_input_context,
            "organisational_framework": test_input_organisational_framework,
        }
    )

    # Check that the build passes
    assert test_output_project.exit_code == 0
    assert test_output_project.exception is None

    # Check there are no `cookiecutter.variable_name` entries in any file
    all_files = [f for f in test_output_project.project_path.rglob("*") if f.is_file()]
    for file in all_files:
        try:
            with open(file, encoding="utf-8") as f:
                assert re.search(r"{+ ?cookiecutter\.\w+ ?}+", f.read()) is None
        except UnicodeDecodeError:
            continue

    # Test that the documentation builds as expected, and then for broken links
    test_output_project_docs_folder = test_output_project.project_path.joinpath("docs")
    assert (
        main(
            [
                "-b",
                "html",
                str(test_output_project_docs_folder),
                str(test_output_project_docs_folder.joinpath("_build")),
            ]
        )
        == 0
    )
