# 2. Person class mein age property + setter jo negative age reject kare.

class Person:
    def __init__(self, age):
        self.age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
person = Person(20)
print(person.age)
person.age = 30
print(person.age)