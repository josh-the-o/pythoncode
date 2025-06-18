import tkinter

hola = tkinter.Tk()
bo = tkinter.Button(hola, text="Don't press this Button", width=100)
bo.pack(padx=400, pady=100)
click = 0


def onClick(event):
    global click
    click = click + 1
    if click == 1:
        bo.configure(text="So you dare to click this Button!?")
    elif click == 2:
        bo.configure(text="Warning:DO NOT CLICK THIS BUTTON OR ELSE....")
    elif click == 3:
        bo.configure(text="Why did you click this button!?I told you not to!")
    elif click == 4:
        bo.configure(text="Because you have clicked this button....")
    elif click == 5:
        bo.configure(text="Your computer has been bricked")
    elif click == 6:
        bo.configure(text="GOOD LUCK fixing your computer hahahahahah")
    elif click == 7:
        bo.configure(text="   ")
    elif click == 8:
        bo.configure(text="Computer.exe has stopped working")
    elif click == 9:
        bo.configure(text="Usb Driver bus has stopped working")
    elif click == 10:
        bo.configure(text="Hardrive corrupted")
    elif click == 11:
        bo.configure(text="Rebooting")
    elif click == 12:
        bo.configure(text=":) :) :)")
    else:
        bo.pack_forget()


bo.bind("<ButtonRelease-1>", onClick)
hola.mainloop()
