from tkinter import *


class RainbowButton:

    def __init__(self, master, color_name, color_code):
        self.color_name = color_name
        self.color_code = color_code
        self.btn = Button(master, bg=color_code, command=self.get_color)
        self.btn.pack(fill=X)

    def get_color(self):
        ent.delete(0, END)
        ent.insert(0, self.color_code)
        lab['text'] = self.color_name


colors = {
    '#ff0000': "Красный",
    '#ff7d00': "Оранжевый",
    '#ffff00': "Желтый",
    '#00ff00': "Зеленый",
    '#007dff': "Голубой",
    '#0000ff': "Синий",
    '#7d00ff': "Фиолетовый"
}

root = Tk()
root.title('Rainbow')
root.iconbitmap('python.ico')
root.geometry('250x220+500+200')
root.resizable(FALSE, FALSE)

lab = Label(root)
lab.pack()
ent = Entry(root, justify='center')
ent.pack(fill=X)

for code, text in colors.items():
    RainbowButton(root, text, code)

root.mainloop()
