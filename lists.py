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

def sumOfAllNumbers(numbers):
    sum = 0
    count = 0;
    for number in numbers:
        try:
            sum += number
            count += 1
        except:
            print(f'{number} is not a valid number!')
    return sum

def countNumbers(numbers):
    count = 0;
    for number in numbers:
        try:
            sum = number + number
            count += 1
        except:
            pass
    return count

def calculateAverageNumbers():
    numbers = [1,2,4,66,89,44, None ,57, 'aaa']
    sum = sumOfAllNumbers(numbers)
    count = countNumbers(numbers)
    return sum / count

print(calculateAverageNumbers())