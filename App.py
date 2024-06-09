from tkinter import *
from app_setting import *
from os import path
from PIL import Image, ImageTk

class App():

    def __init__(self):
        self.window = Tk()
        self.window.geometry(str(w_width) + "x" + str(w_height))
        self.window.title("My App")
        
        self.window.configure(background="black")
        
        self.bottom_frame = Frame(background='black', width=500, height=1000)
        self.bottom_frame.pack(side='left')
        
        button_font = ("Helvetica", 12, "bold") 

        self.home_button = Button(self.bottom_frame, text="Home", height=6, width=30, bg='red', font=button_font)
        self.home_button.place(x=20, y=280)
       
        self.account_button = Button(self.bottom_frame, text="Account", height=6, width=30, bg='red', font=button_font)
        self.account_button.place(x=20, y=80)
        
        self.calendar_button = Button(self.bottom_frame, text="Calendar", height=6, width=30, bg='red', font=button_font)
        self.calendar_button.place(x=20, y=480)
        
        self.shop_button = Button(self.bottom_frame, text='Shop', height=6, width=30, bg='red', font=button_font)
        self.shop_button.place(x=20, y=680)
        
        self.exit_button = Button(self.bottom_frame, text="Exit", height=6, width=30, bg='red', font=button_font, command=self.exit)
        self.exit_button.place(x=20, y=880)
        
        self.space_label = Label(self.window, bg='black', width=20, height=5)
        self.space_label.pack()
        
        self.dirname = path.dirname(__file__)
        self.filename = path.join(self.dirname, 'images/logo.png')
        
        self.load_logo_image()
        
        self.red_box1 = Label(self.window, bg='red', height=10, bd=0, highlightthickness=0, borderwidth=10)
        self.red_box1.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.red_box1.config(width=30, font=("Helvetica", 14, "bold"), text="Activities", padx=20, pady=10, relief='solid', bd=3, borderwidth=2, highlightthickness=0, highlightbackground='black')
        
        self.red_box2 = Label(self.window, bg='red', height=10, bd=0, highlightthickness=0, borderwidth=10)
        self.red_box2.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.red_box2.config(width=30, font=("Helvetica", 14, "bold"), text="Calories Burnt", padx=20, pady=10, relief='solid', bd=3, borderwidth=2, highlightthickness=0, highlightbackground='black')
        
        self.window.mainloop()
        
    def load_logo_image(self):
        original_logo = Image.open(self.filename)

        # Resize the image to an appropriate size
        resized_logo = original_logo.resize((100, 100), Image.LANCZOS)

        # Convert to a PhotoImage to use in Tkinter
        self.logo_img = ImageTk.PhotoImage(resized_logo)

        # Create a label to display the image
        self.logo_label = Label(self.window, image=self.logo_img, bg='black')
        self.logo_label.place(x= 900 , y= 10)

    def exit(self):
        self.window.destroy()

# Run the application
if __name__ == "__main__":
    app = App()
