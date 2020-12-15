def rus_eng(f1,f2):
    ruen=input("Введите слово которое хотите перевести => ")
    if ruen in f1:
        print(f"{ruen} - {f2[f1.index(ruen)]}")
    elif ruen in f2:
        print(f"{ruen} - {f1[f2.index(ruen)]}")
    else:
        print(f"{ruen} Отсуствует!")
        print("При отсутсвии слова, вы можете его добавить в меню! Выбрав 'Добавление перевода' ")


def loe_fail(f):
    fail=open(f,'r', encoding="utf-8-sig")
    mas=[]
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    print(mas)
    return mas

def add_translate(f1,f2, ru, en):
    with open(f1, 'a', encoding="utf-8-sig") as f1: f1.write(ru + '\n')
    with open(f2, 'a', encoding="utf-8-sig") as f2: f2.write(en + '\n')

def recreate(l1,l2,l3,l4):
    ruen = input("Введите слово которое хотите найти => ")
    if ruen in l3:
        print(f"{ruen}")
        with open(l1, encoding="utf-8-sig") as file_in:text = file_in.read()
        nruen = input("Введи новое слово => ")
        text = text.replace(ruen, nruen)
        with open(l1, "w", encoding="utf-8-sig") as file_out:file_out.write(text)
    elif ruen in l4:
        print(f"{ruen}")
        with open(l2, encoding="utf-8-sig") as file_in:text = file_in.read()
        nruen = input("Введи новое слово => ")
        text = text.replace(ruen, nruen)
        with open(l2, "w", encoding="utf-8-sig") as file_out:file_out.write(text)