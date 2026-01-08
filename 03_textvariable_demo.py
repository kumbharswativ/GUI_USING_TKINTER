from tkinter import *
from tkinter import ttk
import time

msg = None
i = -1

L = ["Hello-01", "Hello-10", "Hello-100"]

def change_button_handler():
    global i
    i = (i+1) % len(L)
    msg.set(L[i])
    s = msg.get()
    print(s)

def main():
    global msg

    root_Window = Tk()
    root_Window.title("Feet to meter conversion")

    msg = StringVar()
    LB = ttk.Label(root_Window,textvariable=msg)
    msg.set("START")
    LB.grid(row = 1, column = 1)

    B = Button(root_Window)
    B.configure(text="Change", command = change_button_handler)
    B.grid(row = 1, column=0)

    root_Window.mainloop()

main()

