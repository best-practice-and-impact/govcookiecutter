from {{ cookiecutter.repo_name.lower().replace(' ', '_').replace('-', '_') }}.example_modules.example_module import(
    hello_world,
    print_string,
    print_favourite_number,
)
import yaml

with open("example_config.yml", "r") as file:
    example_config = yaml.safe_load(file)


name = example_config["user_name"]
company = example_config["company"]
favourite_number = example_config["favourite_number"]

hello_string = hello_world(name, company)
print_string(hello_string)
print_favourite_number(favourite_number, name)
