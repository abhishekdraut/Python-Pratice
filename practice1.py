class students:
    def __init__(self):
        print("constructor call")

    def user():
        print("this is user define")

    def max():
        print("this is max function")


class student1:
    def __init__(self):
        print("constructor call 1")

    def min(self):
        print("this is the minimum function ")
        students.max()
        students.user()


if __name__ == "__main__":
    obj1 = student1()
    obj1.min()
