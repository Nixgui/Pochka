import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg') #открытие в отдельном окне для PyCharm
def ochki():
    x1 = np.arange(-9, -1, 0.01)  # x - массив np.array
    x2 = np.arange(1, 9, 0.01)
    x3 = np.arange(-9, -1, 0.01)
    x4 = np.arange(1, 9, 0.01)
    x5 = np.arange(-9, -6, 0.01)
    x6 = np.arange(6, 9, 0.01)
    x7 = np.arange(-1, 1, 0.01)
    y1 = (-0.0625*((x1+5)**2) + 2) # y - массив с формулами
    y2 = (-0.0625*((x2-5)**2) + 2)
    y3 = (0.25*((x3+5)**2) -3)
    y4 = (0.25*((x4-5)**2) - 3)
    y5 = (-((x5+7)**2) + 5)
    y6 = (-((x6-7)**2) + 5)
    y7 = (-0.5*(x7**2) + 1.5)
    plt.subplots()
    plt.grid(True)
    plt.plot(x1,y1,'-r',linewidth=1)
    plt.plot(x2,y2,'-r',linewidth=1)
    plt.plot(x3,y3,'-r',linewidth=1)
    plt.plot(x4,y4,'-r',linewidth=1)
    plt.plot(x5,y5,'-r',linewidth=1)
    plt.plot(x6,y6,'-r',linewidth=1)
    plt.plot(x7,y7,'-r',linewidth=1)
    plt.savefig("my_image.png")
    plt.show()
def zontik():
    x1 = np.arange(-12, 12, 0.01)
    x2 = np.arange(-4, 4, 0.01)
    x3 = np.arange(-12, -4, 0.01)
    x4 = np.arange(4, 12, 0.01)
    x5 = np.arange(-4, -0.3, 0.01)
    x6 = np.arange(-4, -0.2, 0.01)
    y1 = (-0.0555 * (x1 ** 2) + 12)
    y2 = (-0.125 * (x2 ** 2) + 6)
    y3 = (-0.125 * ((x3 + 8) ** 2) + 6)
    y4 = (-0.125 * ((x4 - 8) ** 2) + 6)
    y5 = (2 * ((x5 + 3) ** 2) - 9)
    y6 = (1.5*((x6+3)**2)-10)
    plt.subplots()
    plt.grid(True)
    plt.plot(x1,y1,'-r',linewidth=1)
    plt.plot(x2,y2,'-r',linewidth=1)
    plt.plot(x3,y3,'-r',linewidth=1)
    plt.plot(x4,y4,'-r',linewidth=1)
    plt.plot(x5,y5,'-r',linewidth=1)
    plt.plot(x6,y6,'-r',linewidth=1)
    plt.savefig("my_image.png")
    plt.show()
def babocgka():
    x1 = np.arange(-9, -1, 0.01)
    x2 = np.arange(1, 9, 0.01)
    x3 = np.arange(-9, -8, 0.01)
    x4 = np.arange(8, 9, 0.01)
    x5 = np.arange(-8, -1, 0.01)
    x6 = np.arange(1, 8, 0.01)
    x7 = np.arange(-8, -1, 0.01)
    x8 = np.arange(1, 8, 0.01)
    x9 = np.arange(-8, -2, 0.01)
    x10 = np.arange(2, 8, 0.01)
    x11 = np.arange(-2, -1, 0.01)
    x12 = np.arange(1, 2, 0.01)
    x13 = np.arange(-1, 1, 0.01)
    x14 = np.arange(-1, 1, 0.01)
    x15 = np.arange(-2,0,0.01)
    x16 = np.arange(0, 2, 0.01)
    y1 = (-0.125*((x1+9)**2)+8)
    y2 = (-0.125*((x2-9)**2)+8)
    y3 = (7*((x3+8)**2) +1)
    y4 = (7*((x4-8)**2) +1)
    y5 = (0.0204*((x5+1)**2))
    y6 = (0.0204*((x6-1)**2))
    y7 = (-0.0816*((x7+1)**2))
    y8 = (-0.0816*((x8-1)**2))
    y9 = (0.3333 * ((x9 + 5) ** 2) - 7)
    y10 = (0.3333 * ((x10 - 5) ** 2) - 7)
    y11 = (-2 * ((x11 + 1) ** 2) - 2)
    y12 = (-2 * ((x12 - 1) ** 2) - 2)
    y13 = (-4*(x13**2)+2)
    y14 = (4*(x14**2)-6)
    y15 = (-1.5 * x15+2)
    y16 = (1.5 * x16+2)
    plt.subplots()
    plt.grid(True)
    plt.plot(x1,y1,'-r',linewidth=1)
    plt.plot(x2,y2,'-r',linewidth=1)
    plt.plot(x3,y3,'-r',linewidth=1)
    plt.plot(x4,y4,'-r',linewidth=1)
    plt.plot(x5,y5,'-r',linewidth=1)
    plt.plot(x6,y6,'-r',linewidth=1)
    plt.plot(x7, y7, '-r', linewidth=1)
    plt.plot(x8, y8, '-r', linewidth=1)
    plt.plot(x9, y9, '-r', linewidth=1)
    plt.plot(x10, y10, '-r', linewidth=1)
    plt.plot(x11, y11, '-r', linewidth=1)
    plt.plot(x12, y12, '-r', linewidth=1)
    plt.plot(x13, y13, '-r', linewidth=1)
    plt.plot(x14, y14, '-r', linewidth=1)
    plt.plot(x15, y15, '-r', linewidth=1)
    plt.plot(x16, y16, '-r', linewidth=1)
    plt.savefig("my_image.png")
    plt.show()
def itsecurity():
    fail = open("dannie.txt", "r") #фаил с данными
    mas1 = [] #пустой массив для записи данных
    mas2 = [] #пустой массив для записи данных после запятой
    mas3 = [] #пустой массив для счёта данных (сколько всего объектов в файле)
    for line in fail:
        n = line.find(",") # поиск запятой
        mas1.append(line[0:n].strip()) #запись данных до запятой в масси mas1
        mas2.append(int(line[n + 1:len(line)].strip())) #запись данных в массив после запятой (mas2)
        mas3.append(len(mas1)) #запись количество обьектов в массив mas3
    fail.close() #закрытие файла
    plt.title = "Данные о ИТ безопасности"
    plt.grid(True)
    color_rectangle = np.random.rand(7, 3) #Перетасовка/рандом цвета
    lines=plt.bar(mas3, mas2, color=color_rectangle) #переменная содержащея в себе график с сортировкой и разными цветами
    plt.legend(lines[:mas3[-1]], mas1, bbox_to_anchor=(1.04,0.0,0.2,1), loc="upper left",borderaxespad=1, mode='expand' )
    #тут чуть выше легенда которая отображаеться справа отдельно от графика
    plt.tight_layout(rect=[0, 0, 0.7, 1]) #сжатие самого графика так что бы поместилась легенда
    plt.get_current_fig_manager().window.state('zoomed') #так как поле графика мало для легеды, сделал автоматическое развёртывание ->
    #-> самого графика на полный экран
    plt.interactive(False) #отключение встроеной интерактивности в PyCharm
    plt.savefig("ItGraph.png") #сохрание в изображение
    plt.show() #показ графика
itsecurity()
ochki()
zontik()
babocgka()