class vehicle:

    def __init__(self, passname = "", type = "", seat = ""):
        self.passname = passname
        self.type = type
        self.seat = seat

    def input(self):
        self.passname = input("Enter your name : ")
        self.type = input("Enter the type of bus that you have travelled in :")
        self.seat = input("Enter your seat number : ")

class bus(vehicle):

    def __init__(self, passname = "", type = "", seat = "", color = "", fare = 0):
        self.passname = passname
        self.type = type
        self.seat = seat
        self.color = color
        self.fare = fare

        vehicle.__init__(self, passname, type, seat)

    def input_bus(self):
        self.color = input("Enter color of the bus that you have travelled in : ")
        self.fare = int(input("Enter the fare of the bus : "))

    def print_all(self):
        print("The name of the passenger is ",self.passname)
        print("The type of bus is ",self.type)
        print("The seat number is ",self.seat)
        print("The color of the bus is ",self.color)
        print("The fare of the bus is ",self.fare)

b1 = bus()
b1.input()
b1.input_bus()
b1.print_all()