from tkinter import *
from tkinter.messagebox import showinfo
root = Tk()
linkerFrame = Frame(master=root)
linkerFrame.pack(side=LEFT)
def clicked():
    bericht = 'Dit is een popup'
    showinfo(title='popup', message=bericht)

def toonVenster():
    def close():
        subwindow.withdraw()
    subwindow = Toplevel(master=root)
    button2 = Button(master=subwindow, text='Button 2', command= close)
    button2.pack( pady=10)

button1 = Button(master=linkerFrame, text='Button 1',command=toonVenster)
button1.pack(pady=10)

button3 = Button(master=root, text='Button 3')
button3.pack(side=RIGHT,pady=10)
root.mainloop()
