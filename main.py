from tkinter import *

w_width = 500
w_height = 700

window = Tk()
window.geometry(str(w_width)+ "x" + str(w_height))
window.title("Dieting Daddy")

top_frame = Frame(background= 'orange', width=w_width, height=100)
top_frame.pack()

main_frame = Frame(background= 'white', width=w_width, height=100)
main_frame.pack()

bottom_frame = Frame(background= 'green', width=w_width, height=100)
bottom_frame.pack()

home_button = Button(bottom_frame, text="Home", height=5, width=5, bg='green')
home_button.place(x=0,y=2)

window.mainloop()