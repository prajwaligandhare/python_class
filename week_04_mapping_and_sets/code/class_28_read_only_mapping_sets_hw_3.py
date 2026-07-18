# Ek config dict banao, use MappingProxyType se lock karo, padhne ki koshish (chalega) aur badalne ki koshish (error padho).

from types import MappingProxyType

config = {"fruit" : "apple", "vegitable": "spinach"}

locked = MappingProxyType(config)

print(locked["fruit"])

locked["fruit"] = "mango"

#Output: apple

#TypeError: 'mappingproxy' object does not support item assignment