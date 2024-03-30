oneToTen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

names = ['Luhan', 'Natália', 'Roberto', 'Luane']

years = [2003,2024]


def sumOfEvenNumbers():
    sum = 0
    for number in oneToTen:
        if(number % 2 == 0):
            sum += number
    return sum


def printInDedescendingOrder():
    for i in range(10, 0, -1):
        print(i)

def printMultiplicationTable():
    typpedNumber = int(input("Enter the number: "))
    for number in range(1,10):
        print(f'{typpedNumber} x {number} = {typpedNumber * number}')

printMultiplicationTable()