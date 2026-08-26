# 3.Append mode se ek 4th goal add karo, phir dobara poori file padho.

with open("mygoals.txt", "a", encoding="utf-8") as f:
    f.write("4. Learn AI\n")

with open("mygoals.txt", 'r', encoding="utf-8") as f:
    print(f.read())
