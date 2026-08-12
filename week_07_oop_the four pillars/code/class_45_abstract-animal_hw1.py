# 1. Ek abstract Animal banao with abstract sound(). Dog aur Cat se implement karo.

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self): ...

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

print(Dog().sound())
print(Cat().sound())                
