# 3. 3 objects ki list banao aur print karke dekho __repr__ kaise kaam karta hai.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book {self.title}, {self.author}"
book = [Book("Python", "Guido"), Book("AI", "Asha")]
print(book)       