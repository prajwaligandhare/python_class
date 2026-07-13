import random

print("=====================Secret gussing number=====================")

while True:

    secret_number = random.randint(0, 100)

    #secret_number =  60

    print("To win the game you have only 4 attempts: ")

    for i in range(0, 5):

        print(f"Attempt {i+1} of 4")
        user_guss_nm = int(input("enter the gussing number [0, 10]:  "))

        if user_guss_nm == secret_number:
            print(f" Congratulation!....you geuss the number in {i+1} attempts")
            break

        if user_guss_nm > secret_number:
            print("Too high! Try again.")
        elif user_guss_nm < secret_number:
            print("Too low! Try again.")

        print("--------------------------------------------------------")  

    print("The secret number was: ", secret_number)    

    print("="*50)  

    choice = input("Do you want to continue this program:  (yes/no)")

    if choice == "no":
        break

print("Thank you for playing this game")    
         
  


           