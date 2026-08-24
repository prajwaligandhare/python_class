# 2. Ek custom exception NegativeNumberError banao aur ek function jo negative par use raise kare.

#custome Exception

class NegativeNumberError(Exception):
    "Raised when a negative number is eccountered."
    pass


def check_negative(number):
    if number < 0:
        raise NegativeNumberError(f"Negative number ecountered: {number}")
    return number    

print(check_negative(-10))    