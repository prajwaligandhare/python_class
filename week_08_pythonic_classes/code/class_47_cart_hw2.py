# 2. Cart class mein __len__ add karo jo items ki sankhya de.

#1.step1: Restate: create class Cart & add __len__ , result should be length of words.
#2.step2: Example: c = Cart(), c.add
#3.step3: Pseudocode:
         # 1. create class Cart
         # 2. add __len__
         # 3. print output

class Cart:
    def __init__(self):
        self.items = []
    def add(self, items):
        self.items.append(items)
    def __len__(self):
        return len(self.items)
c = Cart(); c.add('a'); c.add('b'); c.add('c')    
print(len(c))
            
