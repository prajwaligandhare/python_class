# 2.int(input) mein ek try with ValueError aur ek general Exception fallback.

try:
    num = int(input("Enter a number:"))
    print(f"You entered: {num}")
except ValueError:
    print("That's not a valid number!")
except Exception as e:
    print(f"An error occured: {e}")        