from estdconnection import est_connection

cursor = est_connection()
id=input("enter student id ")
sql = f"""
SELECT * FROM STUDENT WHERE ID='{id}'
"""

cursor.execute(sql)
result=  cursor.fetchone()
print(result)