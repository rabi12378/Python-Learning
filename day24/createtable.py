from estdconnection import est_connection
cursor = est_connection()

sql = """
CREATE TABLE STUDENT(
    ID CHAR(20),
    NAME CHAR(20),
    ADDRESS CHAR(20),
    AGE INT
)
"""
cursor.execute(sql)
print("table created successfully")