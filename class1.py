class people:
    def __init__(self):
        print("you are booking your sit for the travelling in the MSRTC")

    def print_tickets(self):
        print("tickets confirmed")


class male:
    def __init__(self,name):
        self.__name = name
        

    
    def print_tickets(self,age):
        
        self.age1=age
        return self.__name,self.age1

    def route(self):
        print(self.__name,'your route is nasik to pune')

        


class female(people):
    def print_tickets1(self):
        print('tickets are booked female travler')

    def route(slef):
        print("your route is pune to nasik")


passenger = male("abhishek")
print(passenger.print_tickets("21"))
passenger.route()
female1=female()
female1.print_tickets()
