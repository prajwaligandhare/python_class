# 2. Ek Student class with name, marks, aur method report() jo report print kare. 2 objects banao.

class Student:
     def __init__(self, name, marks):
        self.name = name
        self.marks = marks

     def report(self):
         print(f" This is {self.name} Report & he got {self.marks} Marks")


student1 = Student('Anshu', 80).report()
student2 = Student('Minu', 90).report()

         

          