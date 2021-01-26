from mysql.connector import MySQLConnection, Error #импортируем модули для подключения к БД
from DBconn import DBconf #Импортируем конфигурации для подключения в БД
import sys
from PySide import QtCore, QtGui #ипортируем GUI
from Beggin_1 import Ui_Window1, Ui_buttons, Ui_Data #Импорт Окон
def show_client(): #Функция для подключения и вывода строк из БД
    global cursor, conn, rows, row, t
    try:
        db_config=DBconf()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT clients.ClientName, hairdresser.HairdresserName, clients.BeginData, clients.EndData "
                       "FROM clients "
                       "INNER JOIN hairdresser ON clients.Hairdresser = hairdresser.ID")
        t=0
        for row in iter_row(cursor, 10):#Вывод 10 строк разом
            t+=1
            rows=row[0],row[1],row[2],row[3]
            if t==1:
                ui2.label_2.setText(row[0])  # Замена пустого текста на то что есть в БД
                ui2.label.setText(row[1])  # Замента пустого текста на то что есть в БД
                ui2.dateTimeEdit.setDateTime(row[2])  # Выставление Даты и Времени начала работы
                ui2.dateTimeEdit_2.setDateTime(row[3])
            if t==2:
                ui2.label_7.setText(row[0])
                ui2.label_15.setText(row[1])
                ui2.dateTimeEdit_5.setDateTime(row[2])
                ui2.dateTimeEdit_13.setDateTime(row[3])
            if t==3:
                ui2.label_8.setText(row[0])
                ui2.label_16.setText(row[1])
                ui2.dateTimeEdit_6.setDateTime(row[2])
                ui2.dateTimeEdit_14.setDateTime(row[3])
            if t==4:
                ui2.label_9.setText(row[0])
                ui2.label_17.setText(row[1])
                ui2.dateTimeEdit_7.setDateTime(row[2])
                ui2.dateTimeEdit_15.setDateTime(row[3])
            if t==5:
                ui2.label_10.setText(row[0])
                ui2.label_18.setText(row[1])
                ui2.dateTimeEdit_8.setDateTime(row[2])
                ui2.dateTimeEdit_16.setDateTime(row[3])
            if t==6:
                ui2.label_11.setText(row[0])
                ui2.label_19.setText(row[1])
                ui2.dateTimeEdit_9.setDateTime(row[2])
                ui2.dateTimeEdit_17.setDateTime(row[3])
            if t==7:
                ui2.label_12.setText(row[0])
                ui2.label_20.setText(row[1])
                ui2.dateTimeEdit_10.setDateTime(row[2])
                ui2.dateTimeEdit_18.setDateTime(row[3])
            if t==8:
                ui2.label_13.setText(row[0])
                ui2.label_21.setText(row[1])
                ui2.dateTimeEdit_11.setDateTime(row[2])
                ui2.dateTimeEdit_19.setDateTime(row[3])
            if t==9:
                ui2.label_14.setText(row[0])
                ui2.label_22.setText(row[1])
                ui2.dateTimeEdit_12.setDateTime(row[2])
                ui2.dateTimeEdit_20.setDateTime(row[3])
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
def acconts(): #Функция для извлечения из БД аккаунтов
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
def iter_row(cursor, size=10): #Функция для вывода конкретного числа строк в память
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row
app = QtGui.QApplication(sys.argv) #Запуск приложения
Window = QtGui.QWidget() #Присваивание виджета к переменноей 1-го окна
ui = Ui_Window1() #присваивание обьектов к виджету
ui.setupUi(Window) # Указание что обьекты привязаны в Виджету (окну)
Form = QtGui.QWidget() ##Присваивание виджета к переменноей 2-го окна
ui1 = Ui_buttons() # Указание что обьекты привязаны в Виджету (окну)
ui1.setupUi(Form) # Указание что обьекты привязаны в Виджету (окну)
Data = QtGui.QWidget() ##Присваивание виджета к переменноей 3-го окна
ui2 = Ui_Data() # Указание что обьекты привязаны в Виджету (окну)
ui2.setupUi(Data) # Указание что обьекты привязаны в Виджету (окну)
Window.show() #Показать Экран (ПС: в самуом низу прописана иницилезация приложения, без него показ окна не произведёться)

def login():# Функция на проверку совподает ли логин и пароль
    acconts() #Функция извлечение данных из БД
    login=ui.LoginText.displayText() #Считывание то что ввели в поле Логин
    password=ui.PasswordText.displayText() #Считавыние поля Пароль
    if login in rowlp[0]:
        if password in rowlp[1]:
            Window.hide() #Скрыть окно входа
            Form.show() #Показать окно Формы (Кнопки для выбора действий с БД)
        else:
            ui.Error.setText("Неверный логин или пароль!") #Вывод если пароли или логин не совпадают
            ui.LoginText.clear() #Очистка полдя Логин
            ui.PasswordText.clear() #Очистка поля Пароль
    else:
        ui.Error.setText("Неверный логин или пароль!") #Вывод если пароли или логин не совпадают
        ui.LoginText.clear() #Очистка полдя Логин
        ui.PasswordText.clear() #Очистка поля Пароль
def ShowClient(): #функция для перехода к третьему окну и вывод там клиентов
    Form.hide() #Скрыть 2-е окно
    Data.show() #Показать 3-е окно (1-е окно скрыто до тех пор пока его не вызовут)
    show_client() #Фукция показа клиентов
ui1.ShowClient.clicked.connect(ShowClient) #Присвоение к кнопке ShowClient по клику ЛКМ обращение к функции ShowClient
ui.pushButton.clicked.connect(login) #Присвоение к кнопке pushButton обращение к функции login
sys.exit(app.exec_()) #Иницелизация приложения (Второго быть не может!)