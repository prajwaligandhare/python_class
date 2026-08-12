# 2. Jaan-boojh kar ek child banao jo sound() na likhe — error padho.

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self): ...

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    pass

print(Dog().sound())
print(Cat().sound())                