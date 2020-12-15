from Func import *
while 1:
    a=int(input("1 - Добавление перевода\n2 - Перевод!\n=> "))
    if a==1:
        t=int(input("Какое количество слов хотите ввести? => "))
        for j in range(t):
            ru=input("Руссое слово => ")
            en=input("Английское слово => ")
            add_translate("rus.txt","eng.txt",ru,en)
    if a==2:
        rus=[]
        eng=[]
        rus=loe_fail("rus.txt")
        eng=loe_fail("eng.txt")
        rus_eng(rus,eng)