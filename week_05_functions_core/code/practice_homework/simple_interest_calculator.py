#Project 3 — Simple Interest Calculator
#EN: Write a function simple_interest(principal, rate, years) that returns the simple interest (P × R × T) / 100. Print interest for ₹10000 at 5% for 3 years.
#हिंदी: एक function simple_interest(principal, rate, years) बनाओ जो simple interest (P × R × T) / 100 return करे। ₹10000 पर 5% की दर से 3 साल का interest print करो।
#Concepts: three parameters, return
#Hint: return (principal * rate * years) / 100.


def simple_interest(principal, rate, years):
    simple_interest = (principal * rate * years) / 100
    return simple_interest


principal = int(input("Enter the principal: "))

rate = float(input("Enter the rate: "))

years = int(input("Enter the years: "))

print(f"The simple interest is {simple_interest(principal, rate, years)}")

