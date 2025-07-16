def check_repo_name_structure(repo_name: str) -> None:
    """Check if the repository name follows the correct structure.

    Args:
        repo_name: The name of the repository to check.

    Raises:
        ValueError: If the repository name does not follow the correct structure.
    """
    print("checking repo name length", repo_name)

    if len(repo_name) > 88:
        print("checking repo name length")
        raise ValueError("Repository name must not exceed 100 characters.")


if __name__ == "__main__":

    # Check the format of the contact email address supplied is a valid one
    check_repo_name_structure("{{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}")
