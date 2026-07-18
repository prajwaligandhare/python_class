#Task 5 — Sum & Average of N Numbers

#User se pehle poochho kitne numbers dega (count). Phir loop mein ek-ek karke numbers lo, 
#unka sum aur average print karo.

#Concepts: for loop, running total, int(input()), :.2f
#Hint: loop se pehle total = 0 banao, andar total = total + num.


count = int(input("Enter the number: "))
total = 0

for n in range(count):
  num = int(input("enter any number:"))
  total = total + num
  average = total/count

print(f"Sum is: {total:.2f}")
print(f"Average is: {average:.2f}")




  