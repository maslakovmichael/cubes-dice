import tkinter as tk
import random
import time

lst = ['b.png', 'b2.png', 'b3.png', 'b4.png', 'b5.png', 'b6.png']

def throw_dice():
    cube = random.choice(lst)
    return cube

def random_pictures(event):
    global p1, p2
    for i in range(11):
        p1 = tk.PhotoImage(file=throw_dice())
        p2 = tk.PhotoImage(file=throw_dice())
        lab_1['image'] = p1
        lab_2['image'] = p2
        root.update()
        time.sleep(0.18)


root = tk.Tk()
root.geometry('400x200+500+200')
root.title('Кубики. Сделай бросок!!')
root.resizable(False, False)
holst = tk.PhotoImage(file='holst.png')
tk.Label(root, image=holst).pack()
root.iconphoto(True, tk.PhotoImage(file='iconka.png'))

p1 = tk.PhotoImage(file=throw_dice())
p2 = tk.PhotoImage(file=throw_dice())
lab_1 = tk.Label(root, image=p1)
lab_2 = tk.Label(root, image=p2)
lab_1.place(relx=0.3, rely=0.5, anchor='center')
lab_2.place(relx=0.7, rely=0.5, anchor='center')

root.bind('<Button-1>', random_pictures)

root.mainloop()