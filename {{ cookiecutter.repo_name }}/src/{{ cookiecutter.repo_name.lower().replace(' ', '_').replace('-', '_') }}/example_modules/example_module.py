def hello_world(name, company):
    """This function returns a welcoming string given and company
    and a persons name.

    Parameters
    ----------
    name : str
        The name you would like to say hello to
    company : str
        The company name to say hello to

    Returns
    -------
    str
        Complete string greating a person and the company

    Raises
    ------
    TypeError
        name is not a str
    TypeError
        company is not a str
    TypeError
        neither company or name are str variables
    """
    if isinstance(name, str) and isinstance(company, str):
        string = "Hello " + name + " and hello everyone at " + company
        return string

    elif not isinstance(name, str):
        raise TypeError("The 'name' variable entered was not a string")

    elif not isinstance(company, str):
        raise TypeError("The 'company' variable entered was not a string")

    else:
        raise TypeError("The 'name' and 'company' variables entered were not strings")


def print_string(string):
    """function that prints a string after validating the input

    Parameters
    ----------
    string : str
        string to print ouy

    Raises
    ------
    TypeError
        If 'string' variable is not a str
    """
    if isinstance(string, str):
        print(string)
    else:
        raise TypeError("The 'string' variable entered was not a string")


def print_favourite_number(favourite_number, name):
    """Function to print sentence of a name and a person favourite number

    Parameters
    ----------
    favourite_number : int
        Integer number to print
    name : str
        Person name to print

    Raises
    ------
    TypeError
        The name variable is not a str
    TypeError
        The favourite_number variable is not an int
    TypeError
        Both the name and favourite_number varibles are not str and int
        respectively.
    """
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
