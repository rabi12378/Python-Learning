class vehicle:
    engine_type="petrol"
    def __init__(self,colour,noofseats):
        self.colour=colour
        self.noofseats=noofseats
        
    def getinfo(self):
        return (f"the vehicle colour is {self.engine_type} type and the clour of the vehicle is {self.colour} and the no. of seats is {self.noofseats}")
    

v1=vehicle("red",48)
v2=vehicle("orange",2)
print(v1.engine_type)
print(v1.colour)
print(v1.getinfo())