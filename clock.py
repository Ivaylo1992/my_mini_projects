from tkinter import *

from tkinter.ttk import *

from time import strftime

root = Tk()
root.title('Clock')


def time():
    string_text = strftime('%H:%M:%S:%p')
    label.config(text=string_text)
    label.after(1000, time)

label = Label(root, font=('Arial', 80), background='black', foreground='cyan')
label.pack(anchor='center')

time()

mainloop()
