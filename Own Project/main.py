from mysql.connector import MySQLConnection, Error
from DBconn import DBconf
def show_client():
    global cursor, conn, row
    try:
        db_config=DBconf()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT clients.ClientName, hairdresser.HairdresserName, clients.BeginData, clients.EndData "
                       "FROM clients "
                       "INNER JOIN hairdresser ON clients.Hairdresser = hairdresser.ID")

        for row in iter_row(cursor, 10):
            print(row[0],row[1],row[2],row[3])

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
def acconts():
    global cursor, conn, row
    try:
        db_config = DBconf()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT Username, Password FROM accounts ")

        for row in iter_row(cursor, 10):
            print(row[0], row[1])

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