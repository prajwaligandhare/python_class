# 3. Employee parent with work(); Developer aur Designer children jo alag-alag work print karein.

class Employee:
    def work(self):
        print("Working In IT Industry")

class Developer(Employee):
    def work(self):
        print("Working on Agentic AI")

class Designer(Employee):
    def working(self):
        print("I'm Agentic AI Designer")

for e in [Developer(), Designer()]:
    print(e.work())



