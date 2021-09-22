key = 0
n = 5

for i in range(1, n+1):
    for j in range(1, (n+1)-i):
        print(" ", end='')

    key = i
    for k in range(1, i+1):
        print(key, end='')
        key = key+1
    
    if i == 1:
        print(end="")
    else:
        key=key-2
        for l in range(1,i):
            print(key ,end="")
            key=key-1
        
   
    print(end="\n")