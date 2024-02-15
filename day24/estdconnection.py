def est_connection():
    import psycopg2
    conn=psycopg2.connect(
        database="studenttest",
        user="postgres",
        password="rajendradad2029",
        host="127.0.0.1",
        port=5432
    )
    conn.autocommit = True
    print("connection established succesfully")
    cursor = conn.cursor()
    return cursor

if __name__ == "__main__":
    est_connection()