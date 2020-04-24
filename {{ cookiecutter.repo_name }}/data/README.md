# `data` folder

Any data that needs to be stored locally should be saved in this location. This folder, and all its sub-folders are not
version-controlled.

The sub-folders should be used as follows:

- `external`: Any data that will **not** be processed at all, such as reference data;
- `raw`: Any raw data before any processing;
- `interim`: Any raw data that has been partially processed and, for whatever reason, needs to be stored before further 
processing is completed; and
- `processed`: Any raw or interim data that has been fully processed into its final state.

The folder paths for these directories are loaded as environment variables by the [`.envrc`](../.envrc) file; to load 
them in Python, use any or all of the following code:

```python
import os

DIR_DATA = os.environ.get("DIR_DATA")
DIR_DATA_EXTERNAL = os.environ.get("DIR_DATA_EXTERNAL")
DIR_DATA_RAW = os.environ.get("DIR_DATA_RAW")
DIR_DATA_INTERIM = os.environ.get("DIR_DATA_INTERIM")
DIR_DATA_PROCESSED = os.environ.get("DIR_DATA_PROCESSED")
```
