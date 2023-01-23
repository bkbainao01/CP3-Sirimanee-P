#คลาสแม่
class Vehicle:
    wheel =0
    licenseNumber = ""
    serialCode = ""

    def turnOnAirConditioner(self):
        print("Turn on: Air")
#การสืบทอด -คลาสลูก
class Car(Vehicle):
    pass
class PickUps(Vehicle):
    pass
class Van(Vehicle):
    pass

car = Car()
car.turnOnAirConditioner()
pickup = PickUps()
car.turnOnAirConditioner()
van = Van()
car.turnOnAirConditioner()





