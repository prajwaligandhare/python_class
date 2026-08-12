# 3. Ek abstract PaymentMethod with abstract pay(amount); Cash aur Card se implement karo.

from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount): ...

class Cash(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} in cash"

class Card(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} in card"

print(Cash().pay(100))
print(Card().pay(100))                