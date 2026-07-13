#Check karo "level" aur "python" palindrome hain ya nahi.

for word in ["level", "python"]:
    if word == word[::-1]:
        print(f"{word} is a palindrome")
    else:
        print(f"{word}: is not a palindrome")    