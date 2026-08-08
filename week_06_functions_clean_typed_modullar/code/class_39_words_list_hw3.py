# 3. Words ki list ["hi","hello","hey","welcome"] 
# mein se sirf 4+ letter waale filter se rakho.

words = ["hi","hello","hey","welcome"]

letters = list(filter(lambda word: len(word) >= 4, words))

print(letters)
