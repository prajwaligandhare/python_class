# 1. BankAccount mein validation add karo taaki balance kabhi negative na ho.

class BankAccount:
    def __init__(self, balance):
          self._balance = balance

    def deposite(self, amount):
        if amount <= 0:
             print("Deposite Ammount shoul be Avialable")

             return 
        self._balance = self._balance + amount
        print(f"Deposited {amount}. Balance: {self._balance}")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds!")  
            return
        self._balance = self._balance - amount
        print(f"Withdrew {amount}. Balance: {self._balance}")


acc = BankAccount(1000)
                         