from Func import *
rus = []
eng = []
rus = loe_fail("rus.txt")
eng = loe_fail("eng.txt")
while 1:
    a=int(input("1-Добавление перевода\n2-Перевод!\n3-Исправление слов\n4-Проверка знаний\n0-Выход\n=> "))
    if a==1:
        t=int(input("Какое количество слов хотите ввести? => "))
        for j in range(t):
            ru=input("Русское слово => ")
            en=input("Английское слово => ")
            add_translate("rus.txt","eng.txt",ru,en)
    if a==2:
        rus_eng(rus,eng)
    if a==0:
        break
    if a==3:
        recreate("rus.txt","eng.txt",rus,eng)
    if a==4:
        print("Слова будут появляться в хаотичном порядке как Русские, так и английские.")
        print("Ваша задача написать правильный перевод слова")
        znanie(rus,eng)