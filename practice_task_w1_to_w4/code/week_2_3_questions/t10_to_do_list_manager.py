#Task 10 — To-Do List Manager (menu loop)

#Ek khaali list todos = [] banao. Ek while True menu chalao: 
# 1) Add 2) Remove 3) Show 4) Quit. User ke choice ke hisaab se task add/remove/show karo. 4 par loop break karo.

#Concepts: while True, match/case (ya if/elif), list .append()/.remove(), break
#Hint: remove karte waqt check karo item list mein hai ya nahi (warna crash), if item in todos:.


todos = []

while True:
   item = input("Enter your choices (add, remove, show, quit): ")

   if item == "add":
      task = input("Enter your task to add: ")
      todos.append(task)
      print(task)

   elif item == "remove":
      task_2 = input("Enter your task to remove: ")  
      todos.remove(task_2)
      print(todos)

   elif item == "show":
      print(todos)

   elif item == "quit":
      break

   else:
      print("Invalid Choice")
       
      
      