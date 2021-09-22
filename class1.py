class people:
    def __init__(self):
        print("you are booking your sit for the travelling in the MSRTC")

    def print_tickets(self):
        print("tickets confirmed")


class male():
    name="piyush"
    age='21'
    
    def print_tickets(self):
        return(self.name)+(" ")+(self.age)

    def route(self):
        print('your route is nasik to pune')

        


class female(people):
    def print_tickets(self):
        print('tickets are booked female travler')

    def route(slef):
        print("your route is pune to nasik")


passenger = male()
names=passenger.print_tickets()
print(names)
