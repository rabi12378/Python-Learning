import json
import os
# from main import FILENAME
FILENAME="day21/crud/students.json"


def create_student():
    id= input("enter the id of the student : ")
    name=input("enter the name of the student : ")
    age = input ("enter the age of the student :")
    address = input ("enter the address of the student :")
    student = dict(id=id, name = name, age = age , address = address)
    if not os.path.exists(FILENAME):
        with open(FILENAME,"w") as fp:
            fp.write (json.dumps([student], indent=2))
    else:
        with open (FILENAME,"r+") as fp :
            students=json.loads(fp.read())
            students.append(student)
            fp.seek(0)
            fp.write(json.dumps(students,indent=2))
    print ("student added successfully!!!")
    wanttocontinue=input("Do you want to continue ? (y/n)")
    return True if wanttocontinue.lower()=="y" else False