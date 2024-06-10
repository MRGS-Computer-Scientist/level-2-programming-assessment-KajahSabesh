from tkinter import *
from app_setting import *
from os import path
from PIL import Image, ImageTk

class App():

    def __init__(self):
        self.window = Tk()

        # Set the window size to resemble a mobile device
        mobile_width = 375
        mobile_height = 667
        self.window.geometry(f"{mobile_width}x{mobile_height}")

        # Center the window on the screen
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (mobile_width / 2))
        y_coordinate = int((screen_height / 2) - (mobile_height / 2))
        self.window.geometry(f"{mobile_width}x{mobile_height}+{x_coordinate}+{y_coordinate}")

        self.window.title("My App")
        self.window.configure(background="black")

        # Header frame for the logo
        self.header_frame = Frame(self.window, background='black', height=100)
        self.header_frame.pack(fill=X, side='top')

        # Bottom frame for navigation buttons
        self.bottom_frame = Frame(self.window, background='black', height=100)
        self.bottom_frame.pack(fill=X, side='bottom')

        button_font = ("Helvetica", 12, "bold") 

        self.home_button = Button(self.bottom_frame, text="Home", bg='red', font=button_font)
        self.home_button.pack(side='left', fill=BOTH, expand=True)

        self.account_button = Button(self.bottom_frame, text="Account", bg='red', font=button_font)
        self.account_button.pack(side='left', fill=BOTH, expand=True)

        self.calendar_button = Button(self.bottom_frame, text="Calendar", bg='red', font=button_font)
        self.calendar_button.pack(side='left', fill=BOTH, expand=True)

        self.shop_button = Button(self.bottom_frame, text='Shop', bg='red', font=button_font)
        self.shop_button.pack(side='left', fill=BOTH, expand=True)

        self.exit_button = Button(self.bottom_frame, text="Exit", bg='red', font=button_font, command=self.exit)
        self.exit_button.pack(side='left', fill=BOTH, expand=True)

        # Load and display the logo
        self.dirname = path.dirname(__file__)
        self.filename = path.join(self.dirname, 'images/logo.png')
        self.load_logo_image()

        # Main content area
        self.content_frame = Frame(self.window, background='black')
        self.content_frame.pack(fill=BOTH, expand=True)

        self.red_box1 = Label(self.content_frame, bg='red', text="Activities", font=("Helvetica", 14, "bold"))
        self.red_box1.pack(pady=20, fill=BOTH, expand=True)

        self.red_box2 = Label(self.content_frame, bg='red', text="Calories Burnt", font=("Helvetica", 14, "bold"))
        self.red_box2.pack(pady=20, fill=BOTH, expand=True)

        self.window.mainloop()

    def load_logo_image(self):
        original_logo = Image.open(self.filename)

        # Resize the image to an appropriate size
        resized_logo = original_logo.resize((50, 50), Image.LANCZOS)

        # Convert to a PhotoImage to use in Tkinter
        self.logo_img = ImageTk.PhotoImage(resized_logo)

        # Create a label to display the image
        self.logo_label = Label(self.header_frame, image=self.logo_img, bg='black')
        self.logo_label.pack(pady=20)

    def exit(self):
        self.window.destroy()

# Run the application
if __name__ == "__main__":
    app = App()
