# `outputs` folder overview

All outputs from the project should be stored here. This folder path for these
directories is loaded as an environment variable by the `.envrc` file; to load them in
Python, use the following code:

```python
import os

# Load environment variables for the `outputs` folder
DIR_OUTPUTS = os.getenv("DIR_OUTPUTS")
```
