# 1. tools.py mein ek aur function add karo: 
#is_palindrome(text: str) -> bool (typed + docstring).

import math

def is_palindrome(text: str) -> bool:
    """
    Check if a given text is a palindrome.
    Args:
        text: The text to check.
    Returns:
        True if the text is a palindrome, False otherwise.
    """
    return text == text[::-1]

print(is_palindrome("madam"))
print(is_palindrome("hello"))
print(is_palindrome("radar"))