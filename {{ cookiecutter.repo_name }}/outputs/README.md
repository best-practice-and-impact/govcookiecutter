# `outputs` folder

All outputs from the project should be stored here. This folder path for these directories is loaded as an environment 
variable by the [`.envrc`](../.envrc) file; to load them in Python, use the following code:

```python
import os

DIR_OUTPUT = os.environ.get("DIR_OUTPUT")
```
