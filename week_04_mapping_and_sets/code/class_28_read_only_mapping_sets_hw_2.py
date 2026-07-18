#Do sets banao aur unka union, intersection, difference print karo.

class_1 = {"Ayushi", "samarth", "pranjali", "Sakhu"}

class_2 = {"Akash", "samarth", "ajju", "sanju", "Sakhu"}

print(class_1 | class_2)

print(class_1 & class_2)

print(class_1 - class_2)


#output: {'Akash', 'Ayushi', 'samarth', 'pranjali', 'Sakhu', 'ajju', 'sanju'}
        #  {'samarth', 'Sakhu'}
        # {'Ayushi', 'pranjali'}