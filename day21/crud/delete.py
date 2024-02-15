import json
filename="day21/crud/students.json"
def delete_student():
    id=input("enter the id :")
    with open (filename,"r") as fp:
        students = json.loads(fp.read())
        for student in students:
            if student["id"] == id :
                students.remove(student)
                break
        else:
            print("INVALID ID ")
            return 
    with open(filename,"w") as fp :
        fp.write(json.dumps(students))
    print("students deleted successfully")
    wanttocontinue=input("Do you want to continue ? (y/n)")
    return True if wanttocontinue.lower()=="y" else False

