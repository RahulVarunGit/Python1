

class Vehicle:
    def __init__(self, make, model) :
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along...")

    def makeAndModel(self):
        print(f"I am a {self.make} {self.model}" )

myVeh = Vehicle("Tesla", "Model Y")
myVeh.moves()
myVeh.makeAndModel()

class Aeroplane(Vehicle):
    def __init__(self, make, model,faa_id):
         super().__init__(make, model)
         self.faa_id = faa_id

    def moves(self):
        print("Flies along ... ")

class Truck(Vehicle):
        pass

myPlane = Aeroplane("Cesna","M12","123")
myPlane.moves()
myPlane.makeAndModel()

myTruck = Truck("Dune","A1")
myTruck.moves()
myTruck.makeAndModel()

print("------------------")
for v in (myVeh, myPlane, myTruck):
     v.makeAndModel()
     v.moves()