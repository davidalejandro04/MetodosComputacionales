"""
Function with Arguments — Greeter Demo
========================================
Simple demonstration of defining a function that accepts
positional arguments and calling it with user-supplied input.
"""


def greet(username: str, greeting: str):
    """Print a personalised greeting message.

    Args:
        username (str): The name of the person to greet.
        greeting (str): The greeting message to include.
    """
    print("Hello, %s — %s" % (username, greeting))


if __name__ == "__main__":
    name = input("What is your name? ")
    greet(name, "Greetings from Computational Methods!")
