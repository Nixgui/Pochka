from mysql.connector import MySQLConnection, Error
from DBconn import DBconf
import sys
from PySide import QtCore, QtGui
from Beggin_1 import Ui_Window1, Ui_buttons, Ui_Data

def show_client():
    global cursor, conn, rows, row
    try:
        db_config=DBconf()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT clients.ClientName, hairdresser.HairdresserName, clients.BeginData, clients.EndData "
                       "FROM clients "
                       "INNER JOIN hairdresser ON clients.Hairdresser = hairdresser.ID")

        for row in iter_row(cursor, 10):
            rows=row[0],row[1],row[2],row[3]

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
def acconts():
    global cursor, conn, rowlp
    try:
        db_config = DBconf()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT Username, Password FROM accounts ")

        for rowlp in iter_row(cursor, 10):
            print(rowlp[0], rowlp[1])

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
app = QtGui.QApplication(sys.argv)
Window = QtGui.QWidget()
ui = Ui_Window1()
ui.setupUi(Window)
Form = QtGui.QWidget()
ui1 = Ui_buttons()
ui1.setupUi(Form)
Data = QtGui.QWidget()
ui2 = Ui_Data()
ui2.setupUi(Data)
Window.show()

def login():
    acconts()
    login=ui.LoginText.displayText()
    password=ui.PasswordText.displayText()
    if login in rowlp[0]:
        if password in rowlp[1]:
            Window.hide()
            Form.show()
        else:
            ui.Error.setText("Неверный логин или пароль!")
            ui.LoginText.clear()
            ui.PasswordText.clear()
    else:
        ui.Error.setText("Неверный логин или пароль!")
        ui.LoginText.clear()
        ui.PasswordText.clear()
def ShowClient():
    Form.hide()
    Data.show()
    show_client()
    print(row[2])
    ui2.label_2.setText(row[0])
    ui2.label.setText(row[1])
    ui2.dateTimeEdit.setDateTime(row[2])
    ui2.dateTimeEdit_2.setDateTime(row[3])
ui1.ShowClient.clicked.connect(ShowClient)
ui.pushButton.clicked.connect(login)
sys.exit(app.exec_())