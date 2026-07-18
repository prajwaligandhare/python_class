#Task 3 — Even ya Odd + Positive/Negative

#User se ek number lo. Batao woh positive/negative/zero hai, AUR even/odd hai (zero ke liye even/odd mat batao).

#Concepts: if/elif/else, modulus %, ternary
#Hint: even/odd ke liye n % 2 == 0. Ek ternary se "Even"/"Odd" choose karo.

# n % 2 != 0 --odd


# number = int(input("Enter any number: "))

# if number % 2 == 0 and number > 0:
#    print(f"You Enter the Number {number} is Even & it's Positive Number")

# elif number % 2 != 0 and number < 0:
#     print(f"You Enter the Number {number} is Odd & it's Negative Number")

# else:
#      print(f"you Enter the Number is Zero: {number}")   


number = int(input("enter any number: "))

if number > 0:
   print(f"You Enter the Number {number} is Positive Number")

elif number < 0:
   print(f"You Enter the Number {number} is Negative Number")

else:
      print(f"You Enter the Number is Zero: {number}")


if number % 2 == 0:
   print(f"You Enter the Number {number} is Even Number")
else:
   print(f"You Enter the Number {number} is Odd Number")   



