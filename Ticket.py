class Person:
    count = 0
    def __init__(self, name, age):
        self.name = name
    def create(self):
        name = input("Enter Ticket Name:")
        print("Go To https://thecode764.github.io Select Discord Button And Sent Ticket Name In general and Ticket Was Create")
    def close(self):
        name = input("Enter Ticket Name:")
        print("Ticket Was Closed")
    def servertickets(self):
        print("Website Support")
        print("Preimum")
Ticket = Person('python', 40)
run = input("Enter Command:")
if run == "Create":
    Ticket.create()
elif run == "Close":
    Ticket.close()
elif run == "View":
    Ticket.servertickets()
