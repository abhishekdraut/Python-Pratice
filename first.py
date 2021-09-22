
name = ["x", "y", "z,", "w"]
result = ['pass', 'fail', 'null']


def first():

    for every_name in name:
        for each_result in result:
            print(every_name, "is ", each_result)
    print("******************************", "\n")


def second():
    for every_result in result:
        for every_name in name:
            print(every_name, "is ", every_result)
    print("******************************", "\n")


choice = input("Enter choice:""\n"
               "For first function press 1""\n"
               "For second function press 2""\n")
choice = int(choice)
if choice == 1:
    print("the first function is ***************")
    first()

elif choice == 2:
    print("the second fuction is ***************")
    second()
