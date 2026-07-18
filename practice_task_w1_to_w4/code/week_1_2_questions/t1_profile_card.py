#Task 1 — Personal Profile Card

#Q.1. User se name, age, city, aur favourite_subject maango (input()). Phir ek saaf profile card f-string se print karo.

#Concepts: variables, input(), int(), f-strings
#Hint: age ko int(input(...)) se lo taaki age + 1 chal sake.


#print("=========Personal Profile Card============")

name = input("Enter your name: ")

age = int(input("Enter your age: "))

city = input("Enter your city: ")

favourite_subject = input("Enter your favourite subject: ")




print("=========Personal Profile Card============")

print(f"Name: {name}")

print(f"Sex: {age} (next year: {age+1}) ")

print(f"Location: {city}")

print(f"Favourite Subject: {favourite_subject}")


print("========This is you're Personal Profile Card========")



#output:
#=========Personal Profile Card============
# Name: Mohan Kumar
# Sex: 32
# Location: Kanpur
# Favourite Subject: Math
# ========This is you're Personal Profile Card========





