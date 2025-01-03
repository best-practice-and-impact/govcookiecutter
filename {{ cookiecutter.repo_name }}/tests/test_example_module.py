import pytest

from {{ cookiecutter.repo_name.lower().replace(' ', '_').replace('-', '_') }}.example_modules.example_module import (
    hello_world,
    print_favourite_number,
    print_string,
)


class TestHelloWorld:
    def test_string_concat(self):
        assert hello_world("Bob", "ONS") == "Hello Bob and hello everyone at ONS"

    def test_name_type_error(self):
        with pytest.raises(TypeError):
            hello_world(1, "ONS")

    def test_company_type_error(self):
        with pytest.raises(TypeError):
            hello_world("Bob", 1)

    def test_name_and_company_type_error(self):
        with pytest.raises(TypeError):
            hello_world(1, 2)


class TestPrintString:
    def test_print_statements(self, capsys):
        print_string("Hello world and hello ONS")
        captured = capsys.readouterr()
        assert captured.out == "Hello world and hello ONS\n"

    def test_type_error(self):
        with pytest.raises(TypeError):
            print_string(1)


class TestPrintFavouriteNumber:
    def test_string_concat(self, capsys):
        print_favourite_number(7, "Bob")
        captured = capsys.readouterr()
        assert captured.out == "Bob's favourite number is 7!\n"

    def test_name_type_error(self):
        with pytest.raises(TypeError):
            print_favourite_number("7", "Bob")

    def test_company_type_error(self):
        with pytest.raises(TypeError):
            print_favourite_number(7, 1)

    def test_name_and_company_type_error(self):
        with pytest.raises(TypeError):
            print_favourite_number("1", 2)
