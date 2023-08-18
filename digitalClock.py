from tkinter import *
from time import strftime

myWindow = Tk()
myWindow.title('Digital Clock')

def time():
    myTime = strftime('%H:%M:%S %p')
    clock.config(text = myTime)
    clock.after(1000, time)


clock = Label(myWindow, font=('Arial Bold', 40), bg = "#473E66", fg = "#BD83B8")

clock.pack(anchor = 'center')

time()

mainloop()
