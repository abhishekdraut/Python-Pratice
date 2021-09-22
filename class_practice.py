class students:
    def name(self):
        print("my name is abhishek")


class girls(students):
    def sirname(self):
        print("my name is sara")


class boys(students):
    def midle_name(self):
        print("middle name is naomi")


class constructor_call:
    def __init__(self, number1, number2):
        print("the constructor is called")
        self.value1 = number1
        self.value2 = number2
        print(self.value1+self.value2)

    def manual_call(self, number1, number2):
        print("the function is called")
        self.value1 = number1
        self.value2 = number2
        print(self.value1+self.value2)


obj2 = boys()
obj1 = girls()

obj1.name()
obj1.sirname()
obj2.midle_name()
obj2.name()

call1 = constructor_call(1, 6)
call1.manual_call(1, 3)
