from mysql.connector import MySQLConnection, Error
from DBconn import DBconf
def show_client(): 
    try:
        db_config=DBconf()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM books")

        for row in iter_row(cursor, 10):
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row
