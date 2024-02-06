# Create a class Person with instance attributes name and age. Create a method get_details in this class 
# to print name and age. 
# Create another class Employee with attributes salary and designation and inherits 
# the Person class. Create a method get_details in this class to print name, age, salary and designation of 
# the Employee.
    
class person:
    humantype="flesh"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def get_details(self):
        return (f"the name and age of the person is {self.name} and {self.age} respectivelyy")




# people=person("rabi",17)
# people2=person("priyanka",78)
# print(people2.get_details())
# print(person.humantype)
# people.name="rabi2"
# print(people.name)


class employee(person):
    def __init__(self,name,age,salary,designation):
        super().__init__(name,age)
        self.salary=salary
        self.designation=designation
    def get_details(self):
        print(super().get_details())
        return(f"the salary and post of the person is{self.salary},{self.designation}")

people=employee("rabi",32,5000,"manager")
print(people.get_details())
    