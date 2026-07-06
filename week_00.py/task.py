name = "Asha"
age = 17
city = "Mumbai"

print(name)
print(age)
print(city)


print("name")
print(name)

score = 10
print(score)
score = 25
print(score)


bill = 2000
friends = 3
each_pay = bill / friends
print(each_pay)


# Radius 7 wale circle ka area nikalo (use 3.14159 * 7 ** 2).
radius = 7
area = 3.14159 * radius ** 2
print(area)


#Ek student ne 500 mein se 425 marks paaye. Percentage print karo.


marks = 425
total = 500
percentage = marks / total * 100
print(f"The percentage is {percentage:1f}%")

# % use karke check karo ki 2026 ko 4 se divide karne par remainder 0 aata hai ya nahi.
print(2026 % 4)

#Strings ko join karna — PURANA tareeka (aur uska dard)
first = "Virat"
last = "kohli"
full = first + " " + last
print(full)


#Apna name aur city store karke f-string se print karo "Hi, I am ___ from ___."

name = "Khushi Kumari"

city = "Kanpur"

print(f"My Name is {name} and I am from {city} city")


#cost = 250 aur qty = 4 store karke total f-string se print karo.

cost = 250

qty = 4

print(f"The total cost is {cost * qty}")

#marks = 367 store karo, 450 mein se percentage 2 decimals ke saath print karo.

marks = 367

total = 450

print(f"The percentage is {marks / total * 100:.2f}%")



age = 20
has_id  = True

print(age >=18 and has_id)

print(age >=18 or has_id)

print(not has_id)


print(type(5))
print(type(3.14))
print(type("Hello"))
print(type(True))


age_text = "20"

print(age_text)

age_number = int(age_text)
print(age_number + 3)

print(str(100))
print(float(5))
print(bool(3.9))



name = input("What is your name? ")
print(f"Hello, {name}!")


age =int( input("your age: "))
print(age + 1)






















