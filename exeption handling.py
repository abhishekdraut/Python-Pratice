try:
    number1 = int(input("Enter the numerator"))
    number2 = int(input("enter the diominator"))
    result = number1/number2
    print(result)

except ZeroDivisionError:
    print("denomintor cant be zero")
    print("program ended")
