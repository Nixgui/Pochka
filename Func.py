import random as r
import pyttsx3
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
engine = pyttsx3.init()
language1='en'
language2='ru'
def rus_eng(f1,f2): #Функция перевода слов
    ruen=input("Введите слово которое хотите перевести => ")
    if ruen in f1:
        print(f"{ruen} - {f2[f1.index(ruen)]}") #Вывод Русский - Английский
        engine.say(f"{ruen} - {f2[f1.index(ruen)]}")
        engine.runAndWait()
    elif ruen in f2:
        print(f"{ruen} - {f1[f2.index(ruen)]}") #Вывод Английский - Русский
        engine.say(f"{ruen} - {f1[f2.index(ruen)]}")
        engine.runAndWait()
    else:
        print(f"{Fore.RED}{ruen} Отсуствует!")
        print(f"{Fore.GREEN}При отсутсвии слова, вы можете его добавить в меню! Выбрав 'Добавление перевода' ")


def loe_fail(f):  #Функция открытия и чтения файла
    fail=open(f,'r', encoding="utf-8-sig")
    mas=[]
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    print(mas)
    return mas

def add_translate(f1,f2, ru, en): #Функция для добавления слова в фаил
    with open(f1, 'a', encoding="utf-8-sig") as f1: f1.write(ru + '\n')
    with open(f2, 'a', encoding="utf-8-sig") as f2: f2.write(en + '\n')

def recreate(l1,l2,l3,l4): #Функция для поиска файла и последующей его замены
    ruen = input("Введите слово которое хотите найти => ")
    if ruen in l3:
        print(f"{ruen}")
        with open(l1, encoding="utf-8-sig") as file_in:text = file_in.read() #Открытие файла и копирование файла в буфер
        nruen = input("Введи новое слово => ")
        text = text.replace(ruen, nruen) # Замена существуещего слова на новое
        with open(l1, "w", encoding="utf-8-sig") as file_out:file_out.write(text) #Очистка файла и запись из буфера + изменённое слово
    elif ruen in l4:
        print(f"{ruen}")
        with open(l2, encoding="utf-8-sig") as file_in:text = file_in.read()
        nruen = input("Введи новое слово => ")
        text = text.replace(ruen, nruen)
        with open(l2, "w", encoding="utf-8-sig") as file_out:file_out.write(text)
def znanie(f1,f2):
    t=int(input("Вберите язык\n1-Русский\n2-Английский\n=> "))
    if t==1:
        kol=int(input("Сколько слов вы хотите перевести? => "))
        koll=kol
        bal=0
        while kol>0:
            try:
                r1=r.choice(f1)
                print(r1,'\n')
                ii=f1.index(r1)
                slovo=input("Введите перевод слова => ")
                ii2=f2.index(slovo)
                if ii==ii2:
                    print(f"{Fore.GREEN}Правильно")
                    print(".....................\n")
                    bal+=1
                    kol-=1
                else:
                    print(f"{Fore.RED}Неправильно")
                    print(".....................\n")
                    kol -= 1
            except:
                TypeError
        print("Вы ответили на",Fore.GREEN + "{:.0%}".format(bal/koll), "правильно")
    if t==2:
        kol = int(input("Сколько слов вы хотите перевести? => "))
        koll = kol
        bal = 0
        while kol > 0:
            try:
                r2 = r.choice(f2)
                print(r2, '\n')
                ii = f2.index(r2)
                slovo = input("Введите перевод слова => ")
                ii2 = f1.index(slovo)
                if ii == ii2:
                    print(f"{Fore.GREEN}Правильно")
                    print(".....................\n")
                    bal += 1
                    kol -= 1
                else:
                    print(f"{Fore.RED}Неправильно")
                    print(".....................\n")
                    kol -= 1
            except:
                TypeError
        print("Вы ответили на", Fore.GREEN + "{:.0%}".format(bal / koll), "правильно")