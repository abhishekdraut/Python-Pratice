def calculateSquare(n):

    return n*n


numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

number = list(result)
print(number)
