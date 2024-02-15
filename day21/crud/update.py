
# import json
# FILENAME="day21/crud/students.json"
# def update_student():
#     student_id=input("enter the id ")
#     whichinfo=input("enter the info you want to update ")
#     newinfo= input (f"enter the {whichinfo}: ")
#     with open (FILENAME,"r+") as fp:
#         students = json.loads(fp.read())
        
#         for student in students:
#             if student["id"] == student_id:
#                 # print(student)
#                 student[whichinfo]=newinfo
#                 break
#         else:
#             print("invalid id")
            
#         fp.seek(0)
#         fp.write(json.dumps(students, indent=2))
#     wanttocontinue=input("Do you want to continue ? (y/n)")
#     return True if wanttocontinue.lower()=="y" else False






import json
FILENAME="day21/crud/students.json"
def update_student():
    student_id=input("enter the id ")
    whichinfo=input("enter the info you want to update ")
    newinfo= input (f"enter the new {whichinfo} : ")
    with open (FILENAME,"r+") as fp:
        students = json.loads(fp.read())
        filteredstuddent= filter(lambda x : x["id"== id , students])
        if filteredstuddent:
            student=filteredstuddent[0]
            student[whichinfo]= newinfo
        else:
            print("invalid studdent id ")
            
            fp.seek(0)
            fp.write(json.dumps(students, indent=2))
   



print("student updated successfully")
# update_student()



  


