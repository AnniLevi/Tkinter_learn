from tkinter import *

root = Tk()
root.title('Registration form')
root.resizable(FALSE, FALSE)

l_login = Label(root, text='Login:').grid(row=0, column=0, padx=10, pady=10, sticky=W)
e_login = Entry(root).grid(row=0, column=1, columnspan=2, padx=10, sticky=W+E)

l_password = Label(root, text='Password:').grid(row=1, column=0, padx=10, sticky=W)
e_password = Entry(root, show='*').grid(row=1, column=1, columnspan=2, padx=10, sticky=W+E)

btn_login = Button(root, text='Enter', padx=5).grid(row=2, column=0, padx=10, pady=10, ipadx=20, sticky=W)
btn_reg = Button(root, text='Registration', padx=5).grid(row=2, column=1, ipadx=5)
btn_forgot = Button(root, text='Forgot password', padx=5).grid(row=2, column=2, padx=10)


root.mainloop()