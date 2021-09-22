class polygon:
    def __init__(self, value):
        self.parameters = value

    def show_value(self):
        print("the parameters you passed are ", self.parameters)

    def print_value(self):
        print("polygon values ")


class tringle(polygon):
    def show_value(self):
        print("the tringle values are ", self.parameters)

    def print_value(self):
        print("the values are printed")

        super().show_value()


class equilateral(polygon):
    def show_value(self):
        print("the values of the equilateral are shown", self.parameters)


t1 = tringle([12, 13])
t1.show_value()
t1.print_value()
