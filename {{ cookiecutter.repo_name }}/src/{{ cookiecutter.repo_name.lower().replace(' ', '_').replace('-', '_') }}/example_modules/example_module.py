def hello_world(name, company):
    if isinstance(name, str) and isinstance(company, str):
        string = "hello " + name + " and hello everyone at " + company
        return string

    elif not isinstance(name, str):
        raise TypeError("The 'name' variable entered was not a string")

    elif not isinstance(company, str):
        raise TypeError("The 'company' variable entered was not a string")

    else:
        raise TypeError("The 'name' and 'company' variables entered were not strings")


def print_string(string):
    if isinstance(string, str):
        print(string)
    else:
        raise TypeError("The 'string' variable entered was not a string")


def print_favourite_number(favourite_number, name):
    if isinstance(name, str) and isinstance(favourite_number, int):
        string = name + "'s favourite number is " + str(favourite_number) + "!"
        print(string)

    elif not isinstance(name, str):
        raise TypeError("The 'name' variable entered was not a string")

    elif not isinstance(favourite_number, int):
        raise TypeError("The 'favourite_number' variable entered was not an integer")

    else:
        raise TypeError(
            "The 'name' and 'favourite_number' variables have incorrect types"
        )
