from ctypes.wintypes import tagMSG
import re
from unicodedata import name
from Gram import gramatica
from tkinter import ttk

import tkinter
import pandas as pd
window = tkinter.Tk()
pd.set_option("display.max_rows", None, "display.max_columns", None)
window.title("Analizador Lexico")
window.geometry("850x350")
window.configure(background='#D7FF90')
s = ttk.Style()
s.theme_use('clam')

# Configure the style of Heading in Treeview widget
s.configure('Treeview.Heading', background="#A1AEFD")
table = ttk.Treeview(window, columns=(
"#1", "#2", "#3"),show='headings') 
table.heading("#1", text="token") 
table.heading("#2", text="valor")
table.heading("#3", text="incidencias")
table.column("#1", width=100)  
table.column("#2", width=150)
table.column("#3", width=100)
table.place(x=450, y=40, height=290)
table.tag_configure('odd', background='#A1DCFD')
table.tag_configure('even', background='#A1FDF0')
def ObtenerCadena():
    table.delete(*table.get_children())
    x= entry.get()
    evaluate(x)
def evaluate(input):
    divided = input.split()
    for i in range(len(gram.reserved)):
        result = re.findall(r""+gram.reserved[i]+"\\b",input)
        if(i%2==0):
            table.insert('','end',values=(gram.tokens[i],result,len(result)),tags=('odd'))
        else:
            table.insert('','end',values=(gram.tokens[i],result,len(result)),tags=('even'))
    for i in range(len(gram.simbols)):
        result = re.findall(gram.simbols[i],input)
        if(i%2==0):
            table.insert('','end',values=(gram.tokens[i+7],result,len(result)),tags=('even'))
        else:
            table.insert('','end',values=(gram.tokens[i+7],result,len(result)),tags=('odd'))
    divided = input.split()
    ids=[]
    for i in range(len(divided)):
        expression = re.compile(f"{gram.id}")
        result2 = re.fullmatch(expression, divided[i])
        if(result2!=None):
            ids.append(divided[i])
    table.insert('','end',values=("IDS",ids,len(ids)),tags=('odd'))

if __name__ == "__main__":
    gram = gramatica()
    entry = ttk.Entry(window)

    entry.config(width=50)
    # Posicionarla en la ventana.
    entry.place(x=120, y=50)

    T = tkinter.Text(window, height = 10, width = 52)
    boton = tkinter.Button(text="verificar tokens", command=ObtenerCadena)
    boton.place(x=150, y=90)
    window.mainloop()

