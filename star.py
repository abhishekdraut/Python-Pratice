value = int(input("enter the row value for star formation"))

for i in range(0, value+1):
    for j in range(0, i):
        print("*", end="")
    print("\n")
