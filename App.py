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
        
        button_font = ("Helvita", 12, "bold") 

        self.home_button = Button(self.bottom_frame, text="Home", height=3, width=15, bg='red', font=button_font)
        self.home_button.place(x=20,y=200)
       
        self.account_button = Button(self.bottom_frame, text="Account", height=3, width=15, bg='red', font=button_font)
        self.account_button.place(x=20,y=100)
        
        self.calander_button = Button(self.bottom_frame, text="Calendar", height=3, width=15, bg='red', font=button_font)
        self.calander_button.place(x=20,y=300)
        
        self.shop_button = Button(self.bottom_frame, text='Shop', height=3, width=15, bg='red', font=button_font)
        self.shop_button.place(x=20,y=400)
        
        self.statistics_button = Button(self.bottom_frame, text='Statistics', height=3, width=15, bg='red', font=button_font)
        self.statistics_button.place(x=20, y=500)
        
        self.exit_button = Button(self.bottom_frame, text="Exit", height=3, width=15, bg='red', font=button_font)
        self.exit_button.place(x=20,y=600)
        
        self.space_label = Label(self.window, bg='black', width=20, height=5)
        self.space_label.pack()
        
        self.activity_box = Label(self.window, text="Activities", bg='red', width=20, height=10)
        self.activity_box.pack()
        
        self.caloriesburnt_box = Label(self.window, text="Calories Burnt", bg='red', width=20, height=10)
        self.caloriesburnt_box.pack()
        
        self.dirname = path.dirname(__file__)
        self.filename = path.join(self.dirname, 'images/')

        print("The path is", self.filename)

        self.window.mainloop()


    def exit(self):
        self.window.destroy()