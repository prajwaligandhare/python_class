#Task 2 — Smart Bill Calculator

#Ek item ka price aur quantity maango. Total nikaalo. Agar total 1000 se zyada hai toh 10% discount lagao, 
#warna koi discount nahi. Final amount 2 decimals ke saath print karo.

#Concepts: arithmetic, if/else, f-string formatting :.2f
#Hint: discount = total * 0.10 sirf tab jab total > 1000.



item_price = int(input("Enter the Item Price: "))

quantity = int(input("Enter the Item Quantity: "))

#formula: total = price * quantity

total_amount = item_price * quantity 

if total_amount > 1000:
   discount = total_amount * 0.10

   final_amount = total_amount - discount

   print(f"total_amount: {total_amount:.2f}")

   print(f"You got 10% discounts {discount} & you're final ammount is: {final_amount:.2f}")

else:
    print(f"You're not getting any discounts & you're final ammount is: {total_amount:.2f}")
    
        
    