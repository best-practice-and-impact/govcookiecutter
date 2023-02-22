def hello_world(name):
    if isinstance(name, str):
        string = "hello world and hello " + name
        return string
    else:
        raise TypeError("The 'name' variable entered was not a string")
