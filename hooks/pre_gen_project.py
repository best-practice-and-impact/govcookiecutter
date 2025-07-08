
def check_repo_name_structure(repo_name: str) -> None:
    """Check if the repository name follows the correct structure.

    Args:
        repo_name: The name of the repository to check.

    Raises:
        ValueError: If the repository name does not follow the correct structure.
    """
    if len(repo_name) > 2:
        raise ValueError(
            "Repository name must not exceed 88 characters."
        )

