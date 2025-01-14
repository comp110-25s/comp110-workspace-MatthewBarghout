"""My first excercise in COMP110!"""

__author__ = "730737376"


def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "Hello, " + name + "!"


if __name__ == "_main_":
    print(greet(name=input("What is your name? ")))
print("Hello, Campers!")
