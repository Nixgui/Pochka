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
def recreate(f1,f2):
