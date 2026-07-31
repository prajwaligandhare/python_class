## step1 >> restate: create simple calculator for +, -, *, /
## step2 >> example: 7+9 = 16
## step3 >> Pseudocode:
            #Take two number input from user
            #Take any operator as input (+, -, *, /)
            #call respective function according to user input operator
            #give final result


## step4 >> Translate: write code in python language  
## step5 >> Trace (dry run):

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2  

print("===========Welcome to the Simple Calculator===========")    
while True:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    operators = input("Enter the operator (+, -, *, /): ")

    if operators == '+':
        print("The addition of two number is: ", add(number1, number2))

    elif operators == '-':
        print("The substraction of two number is: ", sub(number1, number2))

    elif operators == '*':
        print("The multiplication of two number is: ", mul(number1, number2))

    elif operators == '/':
        print("The division of two number is: ", div(number1, number2))

    else:
        print("Invalid operators")

    want_to_continue = input("Do you want to continue? (yes/no): ")
    if want_to_continue == 'no':
        break    

   

print("===========Thank you for using the Simple Calculator===========")


## step5 >> Trace (dry run):

# "===========Welcome to the Simple Calculator==========="
# Enter the first number: 7
# Enter the second number: 9
# Enter the operator (+, -, *, /): +
# The addition of two number is: 16
# Do you want to continue? (yes/no): yes