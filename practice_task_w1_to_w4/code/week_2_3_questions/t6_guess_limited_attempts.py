#Task 6 — Guess with Limited Attempts

#Ek secret number fix karo (secret = 42). User ko sirf 3 chances do guess karne ke. 
#Har galat guess par "Too high" / "Too low" batao. 3 ke andar sahi → "You won", warna → "Game over, number was 42".

#Concepts: while, break, counter, if/elif/else
#Hint: attempts counter rakho, while attempts < 3. Sahi guess par break.


print("*****************Welcome to Secret Number Game*********************")


secret_number = 42
attempts = 0



while attempts < 3:
   guess_number = int(input("Enter the secret number: "))
   attempts = attempts + 1
   print(f"You have {3 - attempts} attempts left")
   if guess_number == secret_number:
     
      print(f"You Won the game, You enter correct secret number: {secret_number}") 
      break

   elif guess_number > secret_number:
         print(f"You enter this number is Too High...!")  

   else:
         print(f"You enter this number is Too Low...!")  

       

print(f"Game over, The secret number was {secret_number}")
         


print("**************************Thank You For Playing this Game****************************")     


