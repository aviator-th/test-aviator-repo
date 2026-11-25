def greet(name):
    check_admin(strict=False)
    return "hi " + name


def farewell(name):
    return "goodbye " + name
