from tkinter import *

root = Tk()

def clicked():
    grondtal = int(entry.get())
    kwadraat = grondtal ** 2
    tekst = 'kwadraat: van {} = {}'
    label['text'] = tekst.format(grondtal,kwadraat)
def clicked2():
    grondtal = int(entry.get())
    wortel = grondtal ** 0.5
    tekst = 'Wortel: van {} = {}'
    label['text'] = tekst.format(grondtal,wortel)
label = Label(master=root, text='Hello World', background='yellow')
label.pack()

button = Button(master=root, text='Druk hier',command=clicked)
button2 = Button(master=root, text='Druk hier2', command = clicked2)
button.pack(pady=10,fill=X,padx= 5)
button2.pack(pady=10,fill=X,padx=5)

entry = Entry(master=root)
entry.pack(padx=10, pady=10)

root.mainloop()
