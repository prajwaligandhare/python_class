#Task 8 — Reverse & Palindrome Check

#User se ek word lo. Use ulta print karo, aur batao woh palindrome hai ya nahi 
#(case ignore karo — "Madam" bhi palindrome hai).

#Concepts: slicing [::-1], .lower(), if/else
#Hint: compare karne se pehle dono ko .lower() kar do.


word = input("Enter any Word: ")

reversed = word[::-1]

print(f"The reversed word is: {reversed}")

if word.lower() == reversed.lower():
   print(f"It's palindrome, {reversed}")

else:
   print(f"It's not palindrome, {reversed}")   

