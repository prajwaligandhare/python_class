#Try karo tuple ka koi item badalne ki — error padho aur ek line likho kyun aaya.

items = ("Champa", 234, "Kumari", 56)

items[1] = 56

print(items)


# We can't change the value of a tuple because it is immutable.

#TypeError: 'tuple' object does not support item assignment.