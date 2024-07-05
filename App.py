from tkinter import *
from os import path
from PIL import Image, ImageTk
from datetime import datetime, timedelta

class App():

    def __init__(self):
        self.window = Tk()

        # Set the window size to resemble a mobile device
        mobile_width = 375
        mobile_height = 850
        self.window.geometry(f"{mobile_width}x{mobile_height}")

        # Center the window on the screen
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (mobile_width / 2))
        y_coordinate = int((screen_height / 2) - (mobile_height / 2))
        self.window.geometry(f"{mobile_width}x{mobile_height}+{x_coordinate}+{y_coordinate}")

        self.window.title("My App")
        self.window.configure(background="black")

        self.main_frame = Frame(self.window, background='black')
        self.main_frame.pack(fill=BOTH, expand=True)
       
        self.signup_frame = Frame(self.window, background='black')
        self.signup_frame.pack(fill=BOTH, expand=True)
        self.signup_frame.pack_forget()
       
        self.build_main_page()
        self.build_signup_page()
       
        self.workout_routines = {}
        self.current_date = datetime.now()
       
        self.window.mainloop()
       
    def build_main_page(self):
       
        # Header frame for the logo
        self.header_frame = Frame(self.main_frame, background='black', height=100)
        self.header_frame.pack(fill=X, side='top')

        # Bottom frame for navigation buttons
        self.bottom_frame = Frame(self.main_frame, background='black', height=100)
        self.bottom_frame.pack(fill=X, side='bottom')

        button_font = ("Helvetica", 12, "bold")

        self.home_button = Button(self.bottom_frame, text="Home", bg='red', font=button_font, command=self.show_main_page)
        self.home_button.pack(side='left', fill=BOTH, expand=True)

        self.calendar_button = Button(self.bottom_frame, text="Calendar", bg='red', font=button_font, command=self.show_calendar_page)
        self.calendar_button.pack(side='left', fill=BOTH, expand=True)

        self.shop_button = Button(self.bottom_frame, text='Diet', bg='red', font=button_font)
        self.shop_button.pack(side='left', fill=BOTH, expand=True)

        self.exit_button = Button(self.bottom_frame, text="Exit", bg='red', font=button_font, command=self.exit)
        self.exit_button.pack(side='left', fill=BOTH, expand=True)

        # Load and display the logo
        self.dirname = path.dirname(__file__)
        self.filename = path.join(self.dirname, 'images/logo.png')
        self.load_logo_image()

        # Main content area
        self.content_frame = Frame(self.main_frame, background='black')
        self.content_frame.pack(fill=BOTH, expand=True)

        self.welcome_label = Label(self.content_frame, bg='black', fg='white', text="", font=("Helvetica", 14, "bold"))
        self.welcome_label.pack(pady=10)

        self.red_box1 = Label(self.content_frame, bg='red', text="Activities", font=("Helvetica", 14, "bold"))
        self.red_box1.pack(pady=20, fill=BOTH, expand=True)

        self.red_box2 = Label(self.content_frame, bg='red', text="Calories Burnt", font=("Helvetica", 14, "bold"))
        self.red_box2.pack(pady=20, fill=BOTH, expand=True)
       
        self.signup_button = Button(self.content_frame, text="Sign Up", bg='green', fg='white', command=self.show_signup_page, font=button_font)
        self.signup_button.pack(pady=10)

    def build_signup_page(self):
        Label(self.signup_frame, text="Sign Up", font=("Helvetica", 24, "bold"), bg='black', fg='white').pack(pady=20)

        self.signup_name = Entry(self.signup_frame, font=("Helvetica", 14))
        self.signup_name.pack(pady=10)
        self.signup_name.insert(0, "Name")

        self.signup_age = Entry(self.signup_frame, font=("Helvetica", 14))
        self.signup_age.pack(pady=10)
        self.signup_age.insert(0, "Age")

        self.signup_weight = Entry(self.signup_frame, font=("Helvetica", 14))
        self.signup_weight.pack(pady=10)
        self.signup_weight.insert(0, "Weight")

        self.signup_height = Entry(self.signup_frame, font=("Helvetica", 14))
        self.signup_height.pack(pady=10)
        self.signup_height.insert(0, "Height")

        self.signup_km_ran = Entry(self.signup_frame, font=("Helvetica", 14))
        self.signup_km_ran.pack(pady=10)
        self.signup_km_ran.insert(0, "How many km you ran today")

        self.signup_build = Entry(self.signup_frame, font=("Helvetica", 14))
        self.signup_build.pack(pady=10)
        self.signup_build.insert(0, "Build you are trying to achieve")

        Button(self.signup_frame, text="Submit", bg='green', fg='white', font=("Helvetica", 14, "bold"), command=self.calculate_calories).pack(pady=20)
        Button(self.signup_frame, text="Back to Home", bg='red', fg='white', command=self.show_main_page, font=("Helvetica", 14, "bold")).pack(pady=10)

    def show_main_page(self):
        self.signup_frame.pack_forget()
        self.main_frame.pack(fill=BOTH, expand=True)

    def show_signup_page(self):
        self.main_frame.pack_forget()
        self.signup_frame.pack(fill=BOTH, expand=True)

    def show_calendar_page(self):
        # Create a new window for the calendar
        self.calendar_window = Toplevel(self.window)
        self.calendar_window.title("Calendar")
        self.calendar_window.geometry(f"375x850+{int((self.window.winfo_screenwidth() / 2) - (375 / 2))}+{int((self.window.winfo_screenheight() / 2) - (850 / 2))}")
        self.calendar_window.configure(background="black")

        Label(self.calendar_window, text="Calendar", font=("Helvetica", 24, "bold"), bg='black', fg='white').pack(pady=20)
        
        self.calendar_frame = Frame(self.calendar_window, bg='black')
        self.calendar_frame.pack(pady=10)

        self.prev_button = Button(self.calendar_frame, text="←", command=self.prev_day, font=("Helvetica", 14, "bold"))
        self.prev_button.grid(row=0, column=0, padx=20)
        
        self.date_label = Label(self.calendar_frame, text=self.current_date.strftime('%Y-%m-%d'), font=("Helvetica", 14), bg='black', fg='white')
        self.date_label.grid(row=0, column=1, padx=20)
        
        self.next_button = Button(self.calendar_frame, text="→", command=self.next_day, font=("Helvetica", 14, "bold"))
        self.next_button.grid(row=0, column=2, padx=20)

        self.workout_text = Text(self.calendar_window, height=15, width=40, font=("Helvetica", 14), bg='white')
        self.workout_text.pack(pady=20)

        if self.current_date.strftime('%Y-%m-%d') in self.workout_routines:
            self.workout_text.insert(END, self.workout_routines[self.current_date.strftime('%Y-%m-%d')])

        Button(self.calendar_window, text="Save", bg='green', fg='white', command=self.save_workout, font=("Helvetica", 14, "bold")).pack(pady=10)
        Button(self.calendar_window, text="Close", bg='red', fg='white', command=self.calendar_window.destroy, font=("Helvetica", 14, "bold")).pack(pady=10)

    def prev_day(self):
        self.current_date -= timedelta(days=1)
        self.date_label.config(text=self.current_date.strftime('%Y-%m-%d'))
        self.update_workout_text()

    def next_day(self):
        self.current_date += timedelta(days=1)
        self.date_label.config(text=self.current_date.strftime('%Y-%m-%d'))
        self.update_workout_text()

    def update_workout_text(self):
        self.workout_text.delete(1.0, END)
        if self.current_date.strftime('%Y-%m-%d') in self.workout_routines:
            self.workout_text.insert(END, self.workout_routines[self.current_date.strftime('%Y-%m-%d')])

    def save_workout(self):
        self.workout_routines[self.current_date.strftime('%Y-%m-%d')] = self.workout_text.get(1.0, END).strip()

    def calculate_calories(self):
        try:
            name = self.signup_name.get()
            km_ran = float(self.signup_km_ran.get())
            calories_burned = km_ran * 60  # 60 calories per km

            self.welcome_label.config(text=f"Welcome, {name}!")
            self.red_box1.config(text=f"Activities: {km_ran} km ran")
            self.red_box2.config(text=f"Calories Burnt: {calories_burned} calories")
           
            self.show_main_page()
        except ValueError:
            self.welcome_label.config(text="Please enter valid information.")

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
