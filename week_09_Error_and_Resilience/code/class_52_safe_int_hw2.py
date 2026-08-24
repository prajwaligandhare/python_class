# 2. Safe int conversion: user input ko int banao, ValueError handle karke "Invalid" bolo.
text = input("Enter a number: ")
try:
    num = int(text)
    print(f"Doubled: {num * 2}")
except ValueError:
    print("Invalid input")