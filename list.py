numbers=[1,2,3,4,5,6,7,8,9,1,2,3,6,7]
index=0

def print_number(index):
    print("the value of the index",index,"is ",numbers[index])


for i in numbers:
    
    if i==3:
        print_number(index)

    index+=1

 