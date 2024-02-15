from estdconnection  import est_connection
cursor=est_connection()

id = input("enter student id : ")
name = input("enter student name : ")
age = int(input("enter student age : "))
address = input("enter student adddress : ")

sql = f"""
INSERT INTO STUDENT (ID, NAME, AGE , ADDRESS) VALUES ('{id}','{name}','{age}','{address}')
"""
cursor.execute(sql)
print("STUDDENT ADDED SUCCESFULLY")