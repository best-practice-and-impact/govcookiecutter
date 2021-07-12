# `data` folder overview

Any data that needs to be stored locally should be saved in this location. This folder,
and its sub-folders, are not version-controlled.

The sub-folders should be used as follows:

- `external`: any data that will not be processed at all, such as reference data;
- `raw`: any raw data before any processing;
- `interim`: any raw data that has been partially processed and, for whatever reason,
  needs to be stored before further processing is completed; and
- `processed`: any raw or interim data that has been fully processed into its final
  state.

The paths for these directories are loaded as environment variables by the
`.envrc` file. To load them in Python, use any or all of the following code:

```python
import os

# Load environment variables for the `data` folder, and its sub-folders
DIR_DATA = os.getenv("DIR_DATA")
DIR_DATA_EXTERNAL = os.getenv("DIR_DATA_EXTERNAL")
DIR_DATA_RAW = os.getenv("DIR_DATA_RAW")
DIR_DATA_INTERIM = os.getenv("DIR_DATA_INTERIM")
DIR_DATA_PROCESSED = os.getenv("DIR_DATA_PROCESSED")
```

[docs-envrc]: ../docs/structure/README.md#envrc
