from tkinter import *

root = Tk()

lab = Label(root, bg='#fff')
lab.pack(pady=10, fill=X)

colors = {
    '#ff0000': "Красный",
    '#ff7d00': "Оранжевый",
    '#ffff00': "Желтый",
    '#00ff00': "Зеленый",
    '#007dff': "Голубой",
    '#0000ff': "Синий",
    '#7d00ff': "Фиолетовый"
}

class MyLabels:

    def __init__(self, master, color):
        self.color = color
        self.label = Label(master, bg=color, width=4, height=2)
        self.label.pack(side=LEFT, padx=1)
        self.label.bind('<Button-1>', lambda event, key='lk': self.get_color(event, key))
        self.label.bind('<Button-3>', lambda event, key='rk': self.get_color(event, key))

    def get_color(self, event, key):
        if key == 'lk':
            lab['bg'] = self.color
        else:
            lab['bg'] = '#fff'

for code, text in colors.items():
    MyLabels(root, code)


root.mainloop()