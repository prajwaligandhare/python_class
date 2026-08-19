# 1. Student class mein __str__ add karo jo "NAME scored MARKS" de.

#step1: Restate: "Student" nam ka class bano __str__ use karke.
#step2: Example: class Student, f"NAME scored MARKS"
#step3: Pseudocode:
#       1. create class
#       2. use str special method
#       3. print with output
#step4: Translate: Write code in python
#step5: dry run (Trace)


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def __str__(self):
        return f"{self.name} Scored {self.marks} marks." 

s1 = Student("Anuj", 60)  

print(s1)