import json
FILENAME="day21/crud/students.json"

# def read_student ():
#     student_id= input("enter the student id  : ")
#     with open(FILENAME, "r") as fp:
#         students= json.loads(fp.read())
#         for student in students:
#             if student["id"] == student_id:
#                 print(student)
#                 break
#         else:
#             print("invalid student id")

#     wanttocontinue=input("Do you want to continue ? (y/n)")
#     return True if wanttocontinue.lower()=="y" else False



def read_student ():
    student_id= input("enter the student id  : ")
    with open(FILENAME, "r") as fp:
        students= json.loads(fp.read())
        filtered_students=list(filter(lambda a : a["id"] == student_id, students))
        if filtered_students:
            print(filtered_students[0])
        else:
            print("invalid student id ")        

    wanttocontinue=input("Do you want to continue ? (y/n)")
    return True if wanttocontinue.lower()=="y" else False

        

    


