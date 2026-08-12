# 3.Ek Password class with _password aur ek check(guess) method jo True/False de.

class Password:
    def __init__(self, password):
        self._password = password

    def check(self, guess):
        self.guess = guess
        if self.guess == self._password:
            return True
        else:
                return False

password1 = Password("amijotio@123")
print(password1.check("sejalim12"))
print(password1.check("amijotio@123"))
