import datetime
import urllib.request
import json
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title('Конвертер валют')
root.geometry('550x180+300+300')
root.resizable(FALSE, FALSE)
root['background'] = '#D9D9D9'

style = ttk.Style()
style.theme_use('alt')  # ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
style.configure('.', font='Arial 10', padding=10)

for i in range(5):
    root.grid_columnconfigure(i, weight=1)

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


def convertation():
    input_to.delete(0, END)
    try:
        amount_from = input_from.get()
        currency_from = list_from.get()
        currency_to = list_to.get()
        for cur_info in json_object:
            if currency_from == 'BYN':
                rate_from = 1
            if currency_to == 'BYN':
                rate_to = 1
            if cur_info['Cur_Abbreviation'] == currency_from:
                rate_from = float(cur_info['Cur_OfficialRate'] / cur_info['Cur_Scale'])
            if cur_info['Cur_Abbreviation'] == currency_to:
                rate_to = float(cur_info['Cur_OfficialRate'] / cur_info['Cur_Scale'])
        amount_to = round(float(amount_from) * rate_from / rate_to, 2)
        input_to.insert(0, amount_to)
    except:
        messagebox.showwarning("Некорректный ввод", 'Введите корректные данные')


convert_date = json_date(json_object)
text_info = ttk.Label(root,
                      text=f'Конвертер валют по курсу Национального банка Республики Беларусь\nна дату {convert_date}',
                      font='Arial 10 bold')
text_info.grid(row=0, column=0, columnspan=5, sticky=W)

currency_list = [cur['Cur_Abbreviation'] for cur in json_object]
currency_list.append('BYN')
list_from = ttk.Combobox(root, values=currency_list, height=5, width=5)
list_from.grid(row=1, column=0)
list_from.set('BYN')

list_to = ttk.Combobox(root, values=currency_list, height=5, width=5)
list_to.grid(row=1, column=4)
list_to.set('USD')

input_from = ttk.Entry(root)
input_from.grid(row=1, column=1)

ttk.Label(root, text='>>>', font='Arial 10 bold').grid(row=1, column=2)

input_to = ttk.Entry(root)
input_to.grid(row=1, column=3)

calc = ttk.Button(root, text='Конвертировать', command=convertation)
calc.grid(row=2, column=1, columnspan=3, sticky=EW, padx=12, pady=20)

root.mainloop()
