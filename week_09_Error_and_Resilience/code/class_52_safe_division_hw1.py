# 1. Safe division: do numbers lo, divide karo, ZeroDivisionError handle karo.

def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by Zero"

print(safe_division(10, 2))
print(safe_division(10, 0))