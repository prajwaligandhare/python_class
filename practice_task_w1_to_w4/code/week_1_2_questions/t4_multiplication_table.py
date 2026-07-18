#Task 4 — Multiplication Table (clean)

#User se ek number n aur ek limit k lo. n ka table 1 se k tak print karo (loop se).

#Concepts: for loop, range(1, k+1), f-string
#Hint: range ka stop exclusive hai — k ko shaamil karne ke liye k + 1 likho.


n = int(input("Enter the number: "))

k= int(input("Enter the limit: "))

for km in range(1, k+1):
    #print(f"{k} * {n}: {k*n}")
    print(f" {n} * {km}: {km*n}")




# num = int(input("Enter the number: "))

# for i in range(1,20):
#     print(f" {num} * {i}: {num*i}")
    
    
   


