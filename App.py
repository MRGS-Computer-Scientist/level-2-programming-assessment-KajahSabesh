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

        self.home_button = Button(self.bottom_frame, text="Home", height=6, width=30, bg='red', font=button_font)
        self.home_button.place(x=20,y=280)
       
        self.account_button = Button(self.bottom_frame, text="Account", height=6, width=30, bg='red', font=button_font)
        self.account_button.place(x=20,y=80)
        
        self.calander_button = Button(self.bottom_frame, text="Calendar", height=6, width=30, bg='red', font=button_font)
        self.calander_button.place(x=20,y=480)
        
        self.shop_button = Button(self.bottom_frame, text='Shop', height=6, width=30, bg='red', font=button_font)
        self.shop_button.place(x=20,y=680)
        
        self.exit_button = Button(self.bottom_frame, text="Exit", height=6, width=30, bg='red', font=button_font)
        self.exit_button.place(x=20,y=880)
        
        self.space_label = Label(self.window, bg='black', width=20, height=5)
        self.space_label.pack()
        
        self.red_box1 = Label(self.window, bg='red', height=10, bd=0, highlightthickness=0, borderwidth=10)
        self.red_box1.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.red_box1.config(width=30, font=("Helvetica", 14, "bold"), text="Activities", padx=20, pady=10, relief='solid', bd=3, borderwidth=2, highlightthickness=0, highlightbackground='black')
        
        self.red_box2 = Label(self.window, bg='red', height=10, bd=0, highlightthickness=0, borderwidth=10)
        self.red_box2.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.red_box2.config(width=30, font=("Helvetica", 14, "bold"), text="Calories Burnt", padx=20, pady=10, relief='solid', bd=3, borderwidth=2, highlightthickness=0, highlightbackground='black')
        
        
        self.dirname = path.dirname(__file__)
        self.filename = path.join(self.dirname, 'images/')

        print("The path is", self.filename)

        self.window.mainloop()


    def exit(self):
        self.window.destroy()