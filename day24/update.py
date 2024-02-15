from estdconnection import est_connection


cursor=est_connection()
id = input('enter studdent id ')
tochange= input("enter the data to change ")
changevalue=input (f"enter new {tochange}")


sql=f"""
UPDATE STUDENT SET {tochange}='{changevalue}' WHERE ID= '{id}'
"""

cursor.execute(sql)
print("student updated succefully")
