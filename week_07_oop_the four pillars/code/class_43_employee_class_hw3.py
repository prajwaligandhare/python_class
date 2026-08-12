# 3. Employee parent (name, salary); Manager child jo super() use kare aur ek team_size add kare.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

em = Employee('rambha', 90000)
print(em.name, em.salary)

m = Manager('Shama', 50000, 10)
print(m.name, m.salary, m.team_size)



       
