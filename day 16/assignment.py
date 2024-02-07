# Create a class Department with parameters name and number_of_students. Create a method total students, which takes department object as a
#  parameter and return the total number of students from all departments.
class department:
    def __init__(self,name,no_students):
        self.name=name
        self.no_students=no_students
    def totalstudents(self,*others):
        students_in_each=[other.no_students for other in others]
        return sum (students_in_each)+(self.no_students)
b1=department("b1",200)
c1=department("b2",300)
d1=department("b3",300)
print(b1.totalstudents(c1))