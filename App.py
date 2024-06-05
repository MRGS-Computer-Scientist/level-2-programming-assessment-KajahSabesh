from tkinter import *
from app_setting import *
from os import *

class App():

    def __init__(self):
        self.window = Tk()
        self.window.geometry(str(w_width)+ "x" + str(w_height))
        self.window.title("My App")
        
        self.window.configure(background="black")
        
        self.bottom_frame = Frame(background='black', width=500, height=1000)
        self.bottom_frame.pack(side='left')

        self.home_button = Button(self.bottom_frame, text="Home", height=2, width=10, bg='red')
        self.home_button.place(x=40,y=100)
       
        self.account_button = Button(self.bottom_frame, text="Account", height=2, width=10, bg='red')
        self.account_button.place(x=40,y=50)
        
        self.calander_button = Button(self.bottom_frame, text="Calendar", height=2, width=10, bg='red')
        self.calander_button.place(x=40,y=150)
        
        self.shop_button = Button(self.bottom_frame, text='Shop', height=2, width=10, bg='red')
        self.shop_button.place(x=40,y=200)
        
        self.exit_button = Button(self.bottom_frame, text="Exit", height=2, width=10, bg='red')
        self.exit_button.place(x=40,y=250)
        
        self.dirname = path.dirname(__file__)
        self.filename = path.join(self.dirname, 'images/')

        print("The path is", self.filename)

        self.window.mainloop()


    def exit(self):
        self.window.destroy()