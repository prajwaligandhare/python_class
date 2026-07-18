#Task 7 — Word & Character Counter

#User se ek sentence lo. Print karo: kitne words hain, kitne characters (spaces chhod kar), aur sentence UPPERCASE mein.

#Concepts: .split(), .replace(), len(), .upper(), .strip()
#Hint: spaces hatane ke liye .replace(" ", "") phir len().


sentence = input("Enter a sentence: ")

print("************************************************")

sentence.strip()

words = len(sentence.split())

characters = len(sentence.replace(" ", ""))

upper = sentence.upper()

#print(f" The Result is: {sentence}, Words:{words}, Characters:{characters}, Uppercase:{upper}")

#print(f"The Sentence is : {sentence}")
print(f"The Number of Words is : {words}")
print(f"The Number of Characters is : {characters}")
print(f"The Sentence in Uppercase is : {upper}")










