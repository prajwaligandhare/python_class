
class Students:
      def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

      def display(self):
          print("***********Students Details***********")
          print("Name:", self.name)
          print("Age:", self.age)
          print("Roll No:", self.roll_no)

name = input("Enter You're Name: ")
age = int(input("Enter You're Age: "))
roll_no = int(input("Enter you're Roll Number: "))

student1 = Students(name, age, roll_no)

student1.display()
