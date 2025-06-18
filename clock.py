import sys
from tkinter import *
import time


def ticking_():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200, ticking_)


root = Tk()
clock = Label(root, font=("chill", 100, "bold"), bg="purple")
clock.grid(row=0, column=1)
ticking_()
root.mainloop()
