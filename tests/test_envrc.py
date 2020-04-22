from itertools import permutations
import os

# Define the cookiecutter directory
DIR_COOKIECUTTER = "{{ cookiecutter.repo_name }}"

# Initialise an empty list to store the expected filepaths
DIRS_EXPECTED = []

# Get all the directories within `DIR_COOKIECUTTER`, including all subfolders (unless they are `docs` subfolders)
for root, dirs, files in os.walk(DIR_COOKIECUTTER):
    if not os.path.join(DIR_COOKIECUTTER, "docs") in root:
        DIRS_EXPECTED += list(map(lambda d: os.path.join(os.getcwd(), root, d), dirs))

# Get the expected environment variable names for the directories in `DIRS_EXPECTED`; we expect directory environment
# variables to start with "DIR_", and then the path from the top-level to the folder in uppercase, where "/" is
# replaced with "_". For example, a folder called "foo" with a sub-folder "bar" should have environment variables
# "DIR_FOO" and "DIR_FOO_BAR", respectively
ENV_DIRS_EXPECTED = [
    "DIR" + p.replace(os.path.join(os.getcwd(), DIR_COOKIECUTTER), "").replace("/", "_").upper() for p in DIRS_EXPECTED
]

# Define the path to `.envrc`
PATH_ENVRC = os.path.join(DIR_COOKIECUTTER, ".envrc")

# Initialise an empty dictionary to store the environment variables
dict_envrc = {}

# Parse the entire `.envrc` file
with open(PATH_ENVRC) as f:
    for line in f.readlines():
        if not (line.startswith("#") or line == "\n"):
            env_name, env_value = line.lstrip("export ").rstrip("\n").split("=", maxsplit=1)
            dict_envrc[env_name] = env_value.replace("$(pwd)", os.path.join(os.getcwd(), DIR_COOKIECUTTER))

# Recursively replace environment variables used in other environment variables
for k1, k2 in permutations(dict_envrc, r=2):
    dict_envrc[k1] = dict_envrc[k1].replace(f"${k2}", dict_envrc[k2])

# Get just the directory environment variables from `dict_envrc`
dict_envrc_dir = {k: v for k, v in dict_envrc.items() if k.startswith("DIR_")}


def test_env_dirs_correct():
    """Test that the .envrc values are correct for each directory environment variable"""
    assert dict_envrc_dir == dict(zip(ENV_DIRS_EXPECTED, DIRS_EXPECTED))


def test_env_dirs_exist():
    """Test that all the directory environment variables exist as actual directories."""
    for p in dict_envrc_dir.values():
        assert os.path.isdir(p), f"Directory does not exist: {p}"
