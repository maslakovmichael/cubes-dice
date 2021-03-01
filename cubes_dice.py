import tkinter as tk
import random
import time

lst = ['b.png', 'b2.png', 'b3.png', 'b4.png', 'b5.png', 'b6.png']

'''Функция, возвращающая рандомную картинку из списка'''
def throw_dice():
    cube = random.choice(lst)
    return cube

'''Функция, вызывающаяся при событии event (нажатие левой кнопки мышы в окне root). 
Производит цикличную смену картинок в лейблах, 
обновление окна root и паузу между итерациями цикла.'''
def random_pictures(event):
    global p1, p2
    for i in range(11):
        p1 = tk.PhotoImage(file=throw_dice())
        p2 = tk.PhotoImage(file=throw_dice())
        lab_1['image'] = p1
        lab_2['image'] = p2
        root.update()
        time.sleep(0.18)

'''Создание окна root, присвоение ему параметров геометрии, титла, и других.
Создание элемента лейбла для холста. Присвоение окну иконки'''
root = tk.Tk()
root.geometry('400x200+500+200')
root.title('Кубики. Сделай бросок!!')
root.resizable(False, False)
holst = tk.PhotoImage(file='holst.png')
tk.Label(root, image=holst).pack()
root.iconphoto(True, tk.PhotoImage(file='iconka.png'))

'''Создание лейблов для картинок кубиков, 
определение их расположения с помощью place() с параметрами'''
p1 = tk.PhotoImage(file=throw_dice())
p2 = tk.PhotoImage(file=throw_dice())
lab_1 = tk.Label(root, image=p1)
lab_2 = tk.Label(root, image=p2)
lab_1.place(relx=0.3, rely=0.5, anchor='center')
lab_2.place(relx=0.7, rely=0.5, anchor='center')

'''Определение метода bind() для события и функции, 
которую это событие вызывает'''
root.bind('<Button-1>', random_pictures)

root.mainloop()