#Mini Project 1 Temperature converter

# print("=== Celsius to Fahrenheit Converter ===")
# celsius =  float(input("enter temperature in Celsius: "))
# fahrenheit = (celsius * 9 / 5) + 32
# print(f"{celsius}°C is {fahrenheit}°F")


#Mini Project 2- Token-cost Estimator (ek AI - flavored project!)

print("=== AI Token Cost Estimator ===")
tokens = int(input("How many tokens?"))
price_per_1000 = float(input("Price per 1000 tokens (in rupees)? "))
cost = (tokens / 1000) * price_per_1000
print(f"Estimated cost: ₹{cost:.2f} ")
