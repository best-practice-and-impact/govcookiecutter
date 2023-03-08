from {{ cookiecutter.repo_name.lower().replace(' ', '_').replace('-', '_') }}.example_modules.example_module import hello_world
import pytest


class TestHelloWorld:
    def test_string_concat(self):
        assert hello_world("ONS") == "hello world and hello ONS"

    def test_type_error(self):
        with pytest.raises(TypeError):
            hello_world(1)
