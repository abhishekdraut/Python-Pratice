class data:
    name="piyush"
    pin=12
    address="shivaji nagar shumalwadi akole"
    age=21

class subdatda(data):
    height=175
    weight=74
    pan=1234567
    data.name="piyush C"
    subname=data.name
    def print_data(self):
        return (str(subdatda.pan)+" "+subdatda.subname)

subdatada1=subdatda()
one=subdatada1.print_data()
print(one)