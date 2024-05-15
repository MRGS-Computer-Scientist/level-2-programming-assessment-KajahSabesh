from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("My App")

window.grid()

hello_label = Label(text="Hello world")
hello_label.grid(column=1, row=1)

bye_label = Label(text="Bye, World")
bye_label.grid(column=1, row=1)

window.mainloop()
