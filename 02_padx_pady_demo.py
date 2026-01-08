from tkinter import *
from tkinter import ttk

def button_handler():
    print("HELLO")

def main():
    root_window = Tk()
    root_window.title("Feet to meter converter")

    master_frame = ttk.Frame(root_window, padding = "3 3 12 12")
    master_frame.grid(row = 0, column = 0, sticky = (N, W, E, S))

    root_window.columnconfigure(0, weight = 1)
    root_window.rowconfigure(0, weight = 1)

    B = ttk.Button(master_frame)
    B.configure(text = "HELLO", command = button_handler)
    B.grid(row = 1, column = 1, padx = 25, pady = 25)

    root_window.mainloop()

main()