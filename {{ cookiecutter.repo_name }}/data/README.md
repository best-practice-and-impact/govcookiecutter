# `data` folder overview

Any data that needs to be stored locally should be saved in this location.

Most data files should not be pushed to your repository, therefore make
sure your .gitignore file excludes your data files from git commits. An
exemption to this may be an example data file that another user may use in
a tutorial for your package.

The paths for these directories are loaded as environment variables by the
`.envrc` file. To load them in Python, use any or all of the following code:

```python
import os

# Load environment variables for the `data` folder, and its sub-folders
DIR_DATA = os.getenv("DIR_DATA")
```
