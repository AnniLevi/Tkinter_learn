from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.geometry('800x500+500+200')
root.title('Text Editor')
root.iconbitmap('nt.ico')


def add_str():
    text_area.insert('0.1', 'Hello!')


def del_str():
    text_area.delete('1.0', END)


def get_str():
    print(text_area.get('1.0', END))


def change_theme(theme):
    text_area['bg'] = theme_colors[theme]['text_bg']
    text_area['fg'] = theme_colors[theme]['text_fg']
    text_area['insertbackground'] = theme_colors[theme]['cursor']
    text_area['selectbackground'] = theme_colors[theme]['select_bg']


def about_program():
    messagebox.showinfo(title='About program', message='Text Editor Program version 0.1')


def program_exit():
    answer = messagebox.askokcancel(title='Exit', message='Close the program?')
    if answer:
        root.destroy()


def open_file():
    file_path = filedialog.askopenfilename(title='Choose file',
                                           filetypes=(('Text file (*.txt)', '*.txt'), ('All files', '*.*')))
    if file_path:
        text_area.delete('1.0', END)
        with open(file_path, encoding='utf-8') as file:
            text_area.insert('1.0', file.read())


def save_file():
    file_path = filedialog.asksaveasfilename(title='Save file',
                                             filetypes=(('Text file (*.txt)', '*.txt'), ('All files', '*.*')))
    with open(file_path, 'w', encoding='utf-8') as file:
        text = text_area.get('1.0', END)
        file.write(text)



# Add menu
main_menu = Menu(root)
root.config(menu=main_menu)

# File
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=program_exit)
main_menu.add_cascade(label='File', menu=file_menu)

# Format
edit_menu = Menu(main_menu, tearoff=0)
edit_menu_sub = Menu(edit_menu, tearoff=0)
edit_menu_sub.add_command(label='Get', command=get_str)
edit_menu_sub.add_command(label='Add', command=add_str)
edit_menu_sub.add_command(label='Delete All', command=del_str)
edit_menu.add_cascade(label='Edit', menu=edit_menu_sub)
edit_menu.add_command(label='Reverse')
edit_menu.add_separator()
edit_menu.add_command(label='Select all')
main_menu.add_cascade(label='Format', menu=edit_menu)

# Help
help_menu = Menu(main_menu, tearoff=0)
help_menu_sub = Menu(help_menu, tearoff=0)
help_menu_sub.add_command(label='Light theme', command=lambda: change_theme('light'))
help_menu_sub.add_command(label='Dark theme', command=lambda: change_theme('dark'))
help_menu.add_cascade(label='Theme', menu=help_menu_sub)
help_menu.add_command(label='About the program', command=about_program)
main_menu.add_cascade(label='Help', menu=help_menu)

# Theme
theme_colors = {
    'dark': {
        'text_bg': '#343b46',
        'text_fg': '#c6dec1',
        'cursor': '#eda756',
        'select_bg': '#4e5a65'
    },
    'light': {
        'text_bg': '#fff',
        'text_fg': '#000',
        'cursor': '#8000ff',
        'select_bg': '#777'
    }
}

# Text area
text_space = Frame(root)
text_space.pack(fill=BOTH, expand=1)

text_area = Text(text_space)
text_area.config(
    font='Arial 10',
    bg=theme_colors['dark']['text_bg'],
    fg=theme_colors['dark']['text_fg'],
    padx=10,
    pady=10,
    wrap=WORD,
    insertbackground=theme_colors['dark']['cursor'],
    selectbackground=theme_colors['dark']['select_bg'],
    width=30,
    spacing3=10
)
text_area.pack(fill=BOTH, expand=1, side=LEFT)

scroll = Scrollbar(text_space, command=text_area.yview)
scroll.pack(fill=Y, side=LEFT)

text_area.config(yscrollcommand=scroll.set)

root.mainloop()
