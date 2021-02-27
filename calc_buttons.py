from tkinter import *

root = Tk()

f = Frame(root)
f.pack(pady=10)

btn_list = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0'
]

row, column = 0, 0

for i in btn_list:
    if i == '0':
        Button(f, text=i, padx=10, pady=5).grid(row=row, columnspan=3)
    else:
        Button(f, text=i, padx=10, pady=5).grid(row=row, column=column)
    column += 1
    if column == 3:
        column = 0
        row += 1

root.mainloop()