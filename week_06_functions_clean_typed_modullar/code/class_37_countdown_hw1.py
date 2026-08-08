# 1. Recursion se 5 se 1 tak countdown karo.

def countdown(n):
    print(n)

    if n == 1:
        print("Countdown Completed")
    countdown(n-1)

countdown(5)   


# 5, 4, 3, 2, 1, Countdown Completed