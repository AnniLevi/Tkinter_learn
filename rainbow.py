from tkinter import *

root = Tk()
root.title('Rainbow')
root.iconbitmap('python.ico')
root.geometry('250x220+500+200')
root.resizable(FALSE, FALSE)

lab = Label(root)
lab.pack()
ent = Entry(root, justify='center')
ent.pack(fill=X)


def add_color(color, code):
    ent.delete(0, END)
    ent.insert(0, code)
    lab['text'] = color


colors = {
    '#ff0000': "Красный",
    '#ff7d00': "Оранжевый",
    '#ffff00': "Желтый",
    '#00ff00': "Зеленый",
    '#007dff': "Голубой",
    '#0000ff': "Синий",
    '#7d00ff': "Фиолетовый"
}

for color_code, color_name in colors.items():
    Button(root, bg=color_code, command=lambda text=color_name, number=color_code: add_color(text, number)).pack(fill=X)


root.mainloop()
