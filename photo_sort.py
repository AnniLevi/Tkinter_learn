from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
from datetime import datetime


def choose_dir():
    dir_path = filedialog.askdirectory()
    entry_path.delete(0, END)
    entry_path.insert(0, dir_path)


def func_start():
    current_path = entry_path.get()
    if current_path:
        for folder, subfolders, files in os.walk(current_path):
            for file in files:
                file_path = os.path.join(folder, file)
                mtime = os.path.getmtime(file_path)
                date = datetime.fromtimestamp(mtime)
                date = date.strftime('%d/%m/%Y')
                date_folder = os.path.join(current_path, date)
                if not os.path.exists(date_folder):
                    os.mkdir(date_folder)
                os.rename(file_path, os.path.join(date_folder, file))
        messagebox.showinfo("Получилось", "Сортировка выполена успешно!")
        entry_path.delete(0, END)
    else:
        messagebox.showwarning("Упс...", "Выберите папку для сортировки")




root = Tk()
root.title('PhotoSort')
root.geometry('500x115')
root['bg'] = '#A6A6A6'

frame = Frame(root, bg='#808080', bd=5)
frame.pack(ipady=10, fill=X)

entry_path = Entry(frame)
entry_path.pack(side=LEFT, ipady=2, padx=5, expand=TRUE, fill=X)

btn_dialog = Button(frame, text='Выбрать папку', command=choose_dir)
btn_dialog.pack(side=LEFT, padx=5)

btn_start = Button(root, text='Старт', command=func_start)
btn_start.pack(padx=10, pady=15, fill=X)

root.mainloop()
