from tkinter import *
import time

root = Tk()

def tick():
    clock.after(200, tick)
    clock['text'] = time.strftime('%H:%M:%S')

clock = Label(root, font='Arial 70')
clock.pack()

tick()

root.mainloop()