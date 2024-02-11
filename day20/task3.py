# # Given a list of students ["jan","jane","hary","alex"] . create a list of dictionaries with random address and random exam marks
# # dump the list to a Json file students.json. again, read the json file and print the address of "hary"

# # import pickle 
# import random
# import json
# students=["jan","jane","hary","alex"] 
# for name in students:
#     name

# with open("day20/student.dat", "wb") as fp:
#     json.loads(students)


# with open("student.dat", "rb") as fp:
#     data = json.loads(fp)

# print(data)  # ["Jon", "Jane", "Hary", "Alex"]
# result = []
# for student_name in data:
#     result.append({"name": student_name, "location": random.SystemRandom("kathmandu","pokhara","butwal"),"marks": random.randint(50,80)})

# print(result)  # [{}, {}, {}, {}]

# with open("output.dat", "wb") as fp:
#     json.loads(result, fp)

# print("Successfully written !!")











# import json


# students=["jan","jane","hary","alex"] 
# student=[dict(name=name,address="ktm",marks=100)for name in students]


# filename="day20/students.json"
# with open (filename,"w") as fp:
#     fp.write(json.dumps(student , indent=2))
# with open (filename , "r") as fp:
#     # studdent=fp.read()
#     studdent=json.loads(fp.read())
# for student in students:
#     if students["name"]=="hary"
#     print(f'address of hary is {}')
# a=input("enter the name you want to know about")



# print(students.a["address"])




















# Given a list of students ["Jon", "Jane", "Hary", "Alex"] create a list of dictionaries with
# random address and random exam marks. Dump the list to a JSON file students.json. Again read the json file
# and print the address of "Hary"

import json
student_names = ["Jon", "Jane", "Hary", "Alex"]
students = [dict(name=name, address="KTM", marks=100) for name in student_names]  # [{}, {}, {}, {}]  # list comp.

filename = "students.json"
with open(filename, "w") as fp:
    fp.write(json.dumps(students, indent=2))

with open(filename, "r") as fp:
    students = json.loads(fp.read())

print(students)
for student in students:
    if student["name"] == "Hary":
        print(f"Address of Hary is {student['address']}")
        break