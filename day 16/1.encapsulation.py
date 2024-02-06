class person :
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def getintel(self):
        return (f"the name is {self.name} and the age is {self.age}")
        
p1=person("rabi",56)
print(p1.getintel())