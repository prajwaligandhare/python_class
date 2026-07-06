
# It will print the inside strings.
print("=== Celsius to Fahrenheit Converter ===")

# Inside of input function strings just display not store in memory
# but user will enter the input (eg. 30) that will be store in celsius variable.
# eg.: a = 5
     #print(a) 
     # 5 will be store in memory block and that block name is give 
     # 'a' and print call to 'a' & will get the ouptput '5'

celsius = float( input("Enter the temperature in Celsius: "))

#formula:
fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius}°C = {fahrenheit}°F")


# MINI PROJECTS -2:

print(" ==== Fahrenheit to Celsius Converter ==== ")

fahrenheit = float(input("Enter the temperature in Fahrenheit:  "))

celsius = (fahrenheit - 32 ) * 5 / 9

print(f"{fahrenheit}°F = {celsius}°C")



# NINI Project 3:

print(" ==== Token Cost Estimators ==== ")

tokens = int(input("How many tokens:"))

price_per_1000 = float(input("Price per 1000 token (in ruppees)"))

cost = (tokens / 1000) * price_per_1000
print(f"Estimated cost: {cost:.2f}")




print(" ==== Cloths cost Stores ====")

cloths = int(input("How many cloths are you buying?"))

price_per_cloths = int(input("Enter the price of per cloths: "))

total_cost = cloths * price_per_cloths

print(f"The total cost is {total_cost} rupees")




print("=== Khandala's temperature ====")

temp = float(input("Enter the everyday temperature in celcius:"))

weekdays = input("Enter the weekdyas:")

celsius = (temp - 32) * 5 / 9

print(f"{weekdays} temperature in celcius is {celsius}°C")



























