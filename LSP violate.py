class Vehicle:
    def drive(self):
        return 'Driving'
    

class Car(Vehicle):
    pass


class Bicycle(Vehicle):
    def drive(self):
        raise Exception("Bicycles don't drive like cars")
        
