#Task 11 — Student Records (list of tuples)

#Ek list of tuples banao: [("Asha", 85), ("Rahul", 92), ("Priya", 78)].
#Har student ka naam aur marks unpacking se print karo. 
#Phir sabse zyada marks waale ka naam batao.

#Concepts: list of tuples, tuple unpacking in for, running max
#Hint: for name, mark in students: — yeh unpacking hai.


students = [("Asha", 85), ("Rahul", 92), ("Priya", 78)]


max_name = students[0][0]
max_marks = students[0][1]

for name, marks in students:
   print(f" {name} : {marks}")
   if marks > max_marks:
      max_marks = marks
      max_name = name

print(f"Top Student: {max_name}")
   

      



