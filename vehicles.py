class vehicle:
    #inititalize a new vehicle object
    def __init__(self, doors, wheels, name):
        self.doors = doors
        self.wheels = wheels
        self.name = name

    #describe what a particular vehicle object is
    def __repr__(self):
        return "%s: %d: doors and %d wheels"%(self.name, self.doors, self.wheels)

    #comparing if 2 vehicles are the same
    def __eq__(self, aveh):
        return self.doors == aveh.doors and self.wheels == aveh.wheels

    #add number of doors of from second vehicle to first vehicle
    def __iadd__(self, aveh):
        self.doors += aveh.doors
        self.wheels += aveh.wheels
        self.name += "+"
        self.name += aveh.name
        return self
