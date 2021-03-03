import datetime
from tkinter import *
import urllib.request
import json
from tkinter import messagebox


root = Tk()
root.title('Курсы валют')
root.resizable(FALSE, FALSE)
root['bg'] = '#BFBFBF'

try:
    html = urllib.request.urlopen('https://www.nbrb.by/api/exrates/rates?periodicity=0')
    data = html.read()
    json_object = json.loads(data)
except:
    messagebox.showerror("Ошибка", 'Ошибка получения курсов валют')


def json_date(json_list):
    json_date = json_list[0]['Date']
    date = datetime.datetime.strptime(json_date, '%Y-%m-%dT%H:%M:%S').strftime('%d.%m.%Y')
    return date

# Header
header_frame = Frame(root, bg='#BFBFBF')
header_frame.pack(fill=X, pady=10)

for i in range(5):
    header_frame.grid_columnconfigure(i, weight=1)

convert_date = json_date(json_object)
text_info = Label(header_frame,
                  text=f'Курсы валют НБ РБ на дату {convert_date}',
                  font='Arial 12 bold',
                  anchor=CENTER,
                  bg='#BFBFBF',
                  pady=5)
text_info.grid(row=1, column=0, columnspan=5, sticky=EW)

# Table of rates
table_frame = Frame(root)
table_frame.pack(fill=X, padx=10)

table_frame.grid_columnconfigure(0, weight=1)
table_frame.grid_columnconfigure(1, weight=1)
table_frame.grid_columnconfigure(2, weight=1)

currency = Label(table_frame, text="Валюта", anchor=W, bg='#D9D9D9', font="Arial 10 bold")
currency.grid(row=0, column=0, sticky=EW)
abbreviation = Label(table_frame, text="Аббревиатура", anchor=CENTER, bg='#D9D9D9', font="Arial 10 bold")
abbreviation.grid(row=0, column=1, columnspan=2, sticky=EW)
rate = Label(table_frame, text="Курс", anchor=E, bg='#D9D9D9', font="Arial 10 bold")
rate.grid(row=0, column=3, sticky=EW)

# Rates in table
row = 1
for currency_info in json_object:
    if row % 2 == 0:
        bg = '#EEEEEE'
    else:
        bg = '#fff'
    cur_name = Label(table_frame, text=currency_info['Cur_Name'], anchor=W, bg=bg, font="Arial 10")
    cur_name.grid(row=row, column=0, sticky=EW)
    cur_coef = Label(table_frame, text=currency_info['Cur_Scale'], anchor=E, bg=bg, font="Arial 10")
    cur_coef.grid(row=row, column=1, sticky=EW)
    cur_abbr = Label(table_frame, text=currency_info['Cur_Abbreviation'], anchor=W, bg=bg, font="Arial 10")
    cur_abbr.grid(row=row, column=2, sticky=EW)
    cur_rate = Label(table_frame, text=currency_info['Cur_OfficialRate'], anchor=E, bg=bg, font="Arial 10")
    cur_rate.grid(row=row, column=3, sticky=EW)
    row += 1

root.mainloop()
