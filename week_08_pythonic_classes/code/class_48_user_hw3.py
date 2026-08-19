# 3.User class mein from_dict classmethod banao.
class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['age'], data['email'])
user = User.from_dict({"name": "Shashi", "age": 20, "email": "shashi@gmail.com"})    
print(user.name, user.age, user.email)    