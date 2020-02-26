# `src` folder

All functions for this project, should be stored in this folder. **All tests should be stored in the 
[`tests`](../tests/README.md) folder**, which is one-level above this folder in the main project directory.

The sub-folders should be used as follows:

- `make_data`: Data processing-related functions;
- `make_features`: Feature-related functions, for example, functions to create features from processed data;
- `make_models`: Model-related functions;
- `make_visualisations`: Functions to produce visualisations;
- `utils`: Utility functions that are helpful in the project.

It is strongly suggested that you import functions in the `src` [`__init__.py`](__init__.py) script, and that you try 
and use absolute imports in this script whenever possible.