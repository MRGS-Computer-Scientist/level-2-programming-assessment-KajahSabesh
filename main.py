from tkinter import *

w_width = 500
w_height = 700

window = Tk()
window.geometry(str(w_width)+ "x" + str(w_height))
window.title("Dieting Daddy")

top_frame = Frame (background= 'red', width=w_width, height=100)
top_frame.pack()

main_frame = Frame(background =bg_color, width=w_width, height=(w_height=200))

