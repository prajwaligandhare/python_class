# 3. Ek try/except/else/finally ka poora example likho jo chaaron blocks dikhaye.

try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print("That's not a valid number!")
else:
    print("Thank you for using the program")
finally:
    print("This block always runs")