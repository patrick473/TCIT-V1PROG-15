from tkinter import *
from treinfuncties import *
def berekenTarief():
    afstand = int(afstandEntry.get())
    prijs = int(standaardprijs(afstand))
    label["text"] = "De ritprijs is: {}".format(prijs)

root = Tk()
afstandEntry = Entry(master=root)
afstandEntry.pack()
button = Button(master=root, text="Druk hier", command=berekenTarief)
button.pack()
label = Label(master=root)
label.pack()
root.mainloop()
