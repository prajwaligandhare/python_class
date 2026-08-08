def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def modulus(a, b):
    return a % b

function_list = ["add", "subtract", "multiply", "divide", "modulus"]

#if __name__ == "__main__":

    #print("Tested successfully")
    #add_Result = add(10, 20)
    #print(f"Add result is: {add_Result}")
    #subtract_Result = subtract(10, 20)
    #print(f"Subtract result is: {subtract_Result}")
    #multiply_Result = multiply(10, 20)
    #print(f"Multiply result is: {multiply_Result}")
    #divide_Result = divide(10, 20)
    #print(f"Divide result is: {divide_Result}")
    #modulus_Result = modulus(10, 20)
    #print(f"Modulus result is: {modulus_Result}")


def is_palindrome(text: str) -> bool:
    """
    Check if a given text is a palindrome.
    Args:
        text: The text to check.
    Returns:
        True if the text is a palindrome, False otherwise.
    """
    return text == text[::-1]

#  print(is_palindrome("madam"))
#print(is_palindrome("hello"))
#print(is_palindrome("radar"))

import math

def circle_area(radius):
       """Return the area of a circle given its radius."""
       return math.pi * radius ** 2