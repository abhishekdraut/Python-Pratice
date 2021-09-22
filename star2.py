#mine
n = 6
space1 = 1

for i in range(1, n+1):
    for j in range(1, n+1-i):
        print(" ", end="")

    if i == 1:
        print("*")
        print(end="\r")

    else:
        print("*"+(space1*" ")+"*")
        space1 = space1+2
        print(end="\r")

for i in range(1,n+1):
    print("* ",end="")

