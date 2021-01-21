from mysql.connector import MySQLConnection, Error
from DBconn import DBconf

def connect():
	global connect
	db_config = DBconf()
	try:
		print("Connecting to MySQL database...")
		connect = MySQLConnection(**db_config)
		if connect.is_connected():
			print("Connection established.")
		else:
			print("Connection failed.")
	except Error as error:
		print(error)
	finally:
		connect.close()
		print("Connection Closed.")

def iter_row(cursor, size=10):
	while True:
		rows = cursor.fetchmany(size)
		if not rows:
			break
		for row in rows:
			yield row
if __name__ == '__main__':
	connect()