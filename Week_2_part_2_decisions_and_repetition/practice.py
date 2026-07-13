print("==============Calculator Program================")

while True:

     num1 = int(input("enter the first number: "))

     num2 = int(input("enter the second number:  "))

     operators = input("enter the operators: +, -, *, %, / : ")

     if operators == '+':
         print(f"addition of {num1} and {num2} is :  ", num1 + num2)

     elif operators == '-':
          print(f"Substrction od {num1} and {num2} is:  ", num1 - num2)

     elif operators == '*':
          print(f"Multiplication of {num1} and {num2} is:  ", num1 * num2)

     elif operators == '%':
          print(f"Modulus of {num1} and {num2} is:  ", num1 % num2)

     elif operators == '/':
          print(f"division of {num1} and {num2} is: ", num1 / num2)

     else:
          print("Invalid Outputs")

     choice = input("Do you want to continue? (yes/no):  ")

     if choice == 'no':
           break

     print("Thank you for using the calculator")
          

