#Project 2 — Temperature Converter
#EN: Write a function celsius_to_f(c) that converts Celsius to Fahrenheit and returns the value. Test it with 0, 37, and 100 degrees.
#हिंदी: एक function celsius_to_f(c) बनाओ जो Celsius को Fahrenheit में बदल कर value return करे। इसे 0, 37 और 100 डिग्री पर test करो।
#Concepts: def, arithmetic, return
#Hint: Formula: (c * 9 / 5) + 32.

## Step1: Restate: create a temperature converter, Celsius to Fahrenheit.
## Step2: Example: F = (0 * 9 / 5) + 32 >> 32.0
## Step3: Pseudocode:
          # Take a celcisus as input from user.
          # call the function & return the value
          # print the result

## Step4: Translate: write code in python
## Step5: Trace (dry run)

## Python code:

def celsius_to_f(c):
    F = (c * 9 / 5) + 32
    return F
c = int(input("Enter the temperature in Celsius: "))
print("The value of Fahrenheit is: ", celsius_to_f(c))    

