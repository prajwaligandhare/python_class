#Apne my_tools.py (Week 5) ke 3 functions mein type 
#hints + Google-style docstrings add karo.

from tkinter import N


def square(n: int) -> int:
    """ Return the square of a number.

Args: 
    n: Te number to square.

Returns:
     n multiplied by itself.
    """
    return n * n

def greet(name: str, greeting: str = "Hi") -> str:
    """ Build a greeting message.
    Args:
        name: Person's name.
        greeting: The greeting word (default "Hi").
    Returns:
        A full greeting string.
    """
    return f"{greeting}, {name}!"        