# Create a class Person with instance attributes name and age. Create a method get_details in this class to print name and age.

class person:
    humantype="flesh"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def get_details(self):
        return (f"the name and age of the person is {self.name} and {self.age} respectivelyy")




people=person("rabi",17)
people2=person("priyanka",78)
print(people2.get_details())
print(person.humantype)
people.name="rabi2"
print(people.name)