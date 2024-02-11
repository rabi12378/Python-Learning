# students=["jon","jane","hary","alex"]
students = ["Jon", "Jane", "Hary", "Alex"]
# Write the above list in a binary file "student.dat"

# Read the binary file and create a dictionary with information of student and their respective exam marks 
# Finally write the info again to the binary file "marks.dat"


# import pickle
# with open("info.dat", "wb") as fp:
#     students = ["Jon", "Jane", "Hary", "Alex"]
# with open("info.dat", "wb") as fp:
#     pickle.dump(students, fp)

# with open ("students.")
    

# print("Successful !!")







"""

students = ["Jon", "Jane", "Hary", "Alex"]
# Write the above list in a binary file "student.dat"

# Read the binary file and create a dictionary with information of student and their respective exam marks
# Finally write the info again to the binary file "marks.dat"

"""
import pickle
import random

students = ["Jon", "Jane", "Hary", "Alex"]
with open("day20/student.dat", "wb") as fp:
    pickle.dump(students, fp)


with open("student.dat", "rb") as fp:
    data = pickle.load(fp)

print(data)  # ["Jon", "Jane", "Hary", "Alex"]
result = []
for student_name in data:
    result.append({"name": student_name, "marks": random.randint(50, 90)})

print(result)  # [{}, {}, {}, {}]

with open("output.dat", "wb") as fp:
    pickle.dump(result, fp)

print("Successfully written !!")