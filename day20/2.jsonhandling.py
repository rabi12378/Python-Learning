# JSON stands for JavaScript Object Notation
# It is a file format to store data so that it could be rendered and parsed easily
# it looks imilar to the python dictionary
# they are mostly used to share infpormation among different entities (Frontend and Backend, Mobile and BAckend, Bachend and Backend)
# Python has a built in JSON _ Module





import json
filename="day20/student.json"

student={"name":"rabi","age":34,"address":"kapan"}

with open(filename,"w") as fp :
    data = json.dumps(student)
    fp.write(data)
with open (filename ,"r") as fp:
    student=fp.read()
    student = json.loads(student)
print(student)