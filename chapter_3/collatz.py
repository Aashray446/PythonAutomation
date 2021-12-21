
def collatz(number):
    if number == 1:
        return
    elif number % 2 == 0:
        print(int(number / 2))
        collatz(number / 2)
    else:
        print(int(number * 3 + 1))
        collatz(number * 3 + 1)
collatz(int(input("Enter any number")))