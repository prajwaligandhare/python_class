#Project 5 — Tip Calculator
#EN: Write a function tip_amount(bill, percent) that returns how much tip to pay. Then print the total bill (bill + tip) for a ₹800 bill at 10%.
#हिंदी: एक function tip_amount(bill, percent) बनाओ जो tip की रकम return करे। फिर ₹800 के bill पर 10% tip के साथ कुल bill (bill + tip) print करो।
#Concepts: return, using the returned value in more maths
#Hint: return bill * percent / 100, then total = bill + tip_amount(800, 10).


def tip_amount(bill, percent):
    tip = bill * percent / 100
    return tip

bill = int(input("Enter the bill value: "))

percent = int(input("Enter the percentage: "))

total = bill + tip_amount(bill, percent)

print(f"The total bill is : {total:.0f}")


