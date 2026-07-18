#2. Ek comma-separated string ko list mein todo, phir " - " se dobara jodo.


names = "pushpa,savita,reena"

#characters = list(names)
words = names.split(",")
print(words)
print("-".join(words))

