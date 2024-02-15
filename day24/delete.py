from estdconnection import est_connection
cursor = est_connection()

id=(input('enter the student id '))


sql = """
DELETE FROM STUDENT WHERE ID = '{id}'
"""
cursor.execute(sql)
print("student deleted successfully")