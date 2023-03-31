# Using pytest

We use [`pytest`][pytest] to create and run all of our python based testing. Pytest is the most commonly used python module for testing python code. Testing your code is vital for followling coding best practices and has numerous benefits such as:

* They help to debug your code
* They make your write more efficient code first time
* They make you think about what precisely your code is doing as you right it
* They provide a sort of documentation for your code
* They help to keep your deployment smooth.

## Structure

There should be a `tests` folder in the root directory of your repository containing all the tests that relate to your package. It sits outside of your package because users that want to just use your package will not necessarily need the tests. The tests are there for contributers to use, and if they are contributing they will clone the whole repository, not just the package.

There is an example pytest folder structure and file in your package that demonstrates this structure.

## Writing pytests

For pytest to find your tests, all test files and tests must either start with `test_` or finish with `_test.py`

The `test_example_module.py` example test file provides an example of these restrictions.

## Running pytest
### In the terminal

There are a few ways to run pytests in your terminal. The easiest is by running
```shell
pytest
```
in your root directory. This will find any existing pytests within your directory and run them.

If you only want to run pytests in a specific pytest file you can run
```shell
pytest tests/test_example_module.py
```

You can try both of these in the root directory of your new repository.


[pytest]: https://pypi.org/project/pytest/
