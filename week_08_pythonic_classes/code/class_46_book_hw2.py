# 2. Book class (title, author) mein __repr__ add karo.

#step1: Restate: create a class gives two parameters and add __repr__.
#step2: Example: class Book, add two paramertes(title, authore) &  add __repr__.
#step3: Pseudocode:
       #1. create a class
       #2. gives two related parameters
       #3. add special method __repr__

#step4: Translate: Write code in python
#tep5: Dry Run (Trace).   


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __repr__(self):
        return f"The Title is {self.title} & Author is {self.author}"

print(Book("Love In Air", "Mr.Zakash"))   