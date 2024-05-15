from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("My App")

hello_label = Label(text="Hello world")
hello_label.pack(side="left")

window.mainloop()
