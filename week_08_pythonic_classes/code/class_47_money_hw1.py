# 1. Money class (amount) mein __eq__ add karo taaki same amount equal ho.

# step1: Restate: create class Money with amount attribute and __eq__ method to compare amounts.
# step2: Example: print(Money(100) == Money(100)) should return True.
# step3: Pseudocode:
        # 1. create class Money with amount attribute.
        # 2. add __eq__ method to compare amounts.
        # 3. print(Money(100) == Money(100)) should return True.
        # 4. print(Money(50) == Money(60)) should return False.

# step4: Translate in python code        

# step5: dry run (Trace the code)        

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

print(Money(100) == Money(100))

print(Money(50) == Money(60))


