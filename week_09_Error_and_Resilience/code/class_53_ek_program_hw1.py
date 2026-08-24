# 1. Ek program jo list se index access kare, ValueError aur IndexError dono alag handle kare.

numbers = [1, 2, 3, 4, 5]

try:
    index  = int(input("Enter an index: "))
    print(numbers[index])
except ValueError:
    print("That's not a valid number!")

except IndexError:
    print("That's not a valid index!")