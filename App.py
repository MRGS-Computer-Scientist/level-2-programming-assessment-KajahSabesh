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

        self.shop_button = Button(self.bottom_frame, text='Diet', bg='red', font=button_font, command=self.show_diet_page)
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

        # Instructional label for the workout text box
        Label(self.calendar_window, text="Enter your workout routine for the selected day below:", font=("Helvetica", 11), bg='black', fg='white').pack(pady=10)

        self.workout_text = Text(self.calendar_window, height=15, width=40, font=("Helvetica", 14), bg='white')
        self.workout_text.pack(pady=20)

        if self.current_date.strftime('%Y-%m-%d') in self.workout_routines:
            self.workout_text.insert(END, self.workout_routines[self.current_date.strftime('%Y-%m-%d')])

        Button(self.calendar_window, text="Save", bg='green', fg='white', command=self.save_workout, font=("Helvetica", 14, "bold")).pack(pady=10)
        Button(self.calendar_window, text="Close", bg='red', fg='white', command=self.calendar_window.destroy, font=("Helvetica", 14, "bold")).pack(pady=10)

    def show_diet_page(self):
        # Create a new window for the diet
        self.diet_window = Toplevel(self.window)
        self.diet_window.title("Diet and Exercise")
        self.diet_window.geometry(f"375x850+{int((self.window.winfo_screenwidth() / 2) - (375 / 2))}+{int((self.window.winfo_screenheight() / 2) - (850 / 2))}")
        self.diet_window.configure(background="black")

        Label(self.diet_window, text="Diet and Exercise", font=("Helvetica", 24, "bold"), bg='black', fg='white').pack(pady=20)

        # Survey for selecting focus
        self.focus_var = StringVar(value="general_health")

        Label(self.diet_window, text="What do you want to focus on?", font=("Helvetica", 14), bg='black', fg='white').pack(pady=10)

        Radiobutton(self.diet_window, text="General Health", variable=self.focus_var, value="general_health", font=("Helvetica", 14), bg='black', fg='white', selectcolor='black').pack(anchor=W, padx=20)
        Radiobutton(self.diet_window, text="Endurance Improvement", variable=self.focus_var, value="endurance_improvement", font=("Helvetica", 14), bg='black', fg='white', selectcolor='black').pack(anchor=W, padx=20)
        Radiobutton(self.diet_window, text="Muscle Gain", variable=self.focus_var, value="muscle_gain", font=("Helvetica", 14), bg='black', fg='white', selectcolor='black').pack(anchor=W, padx=20)
        Radiobutton(self.diet_window, text="Weight Loss", variable=self.focus_var, value="weight_loss", font=("Helvetica", 14), bg='black', fg='white', selectcolor='black').pack(anchor=W, padx=20)

        Button(self.diet_window, text="Submit", bg='green', fg='white', command=self.submit_focus, font=("Helvetica", 14, "bold")).pack(pady=20)
        Button(self.diet_window, text="Close", bg='red', fg='white', command=self.diet_window.destroy, font=("Helvetica", 14, "bold")).pack(pady=10)

        # Text box to display diet and exercise recommendations
        self.recommendation_text = Text(self.diet_window, height=15, width=40, font=("Helvetica", 12), bg='white')
        self.recommendation_text.pack(pady=20)

    def load_logo_image(self):
        self.logo_image = Image.open(self.filename)
        self.logo_image = self.logo_image.resize((150, 150), Image.LANCZOS)
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)

        self.logo_label = Label(self.header_frame, image=self.logo_photo, bg='black')
        self.logo_label.pack(pady=10)

    def calculate_calories(self):
        print(f"Name: {self.signup_name.get()}")
        print(f"Age: {self.signup_age.get()}")
        print(f"Weight: {self.signup_weight.get()}")
        print(f"Height: {self.signup_height.get()}")
        print(f"KM Ran: {self.signup_km_ran.get()}")
        print(f"Build Goal: {self.signup_build.get()}")

        self.show_main_page()

    def prev_day(self):
        self.current_date -= timedelta(days=1)
        self.date_label.config(text=self.current_date.strftime('%Y-%m-%d'))
        self.load_workout()

    def next_day(self):
        self.current_date += timedelta(days=1)
        self.date_label.config(text=self.current_date.strftime('%Y-%m-%d'))
        self.load_workout()

    def save_workout(self):
        date_str = self.current_date.strftime('%Y-%m-%d')
        self.workout_routines[date_str] = self.workout_text.get("1.0", END).strip()
        print(f"Saved workout for {date_str}: {self.workout_routines[date_str]}")

    def load_workout(self):
        date_str = self.current_date.strftime('%Y-%m-%d')
        self.workout_text.delete("1.0", END)
        if date_str in self.workout_routines:
            self.workout_text.insert(END, self.workout_routines[date_str])
        print(f"Loaded workout for {date_str}: {self.workout_text.get('1.0', END).strip()}")

    def submit_focus(self):
        focus = self.focus_var.get()
        print(f"User selected focus: {focus}")

        recommendations = {
            "general_health": "For general health eat a eat a balanced diet rich in fruits, vegetables, whole grains, and lean proteins thus have a breakfast of porridge with fruit, for lunch have tuna sandwitches and for dinner have brown rice, mixed vegetables, and chicken. For exercise I would suggest going for a walk, run, jog or cycling for 3 hours every week or using a treadmill for the same effect",
            "endurance_improvement": "For endurence improvement eat a diet consisting of complex carbohydrates, lean proteins, and healthy fats thus have a breakfast of toast with poached eggs, for lunch have chicken breast with quinoa, brocolis and tomatoes ; and for dinner have baked salmon with potato mash. In order to increase endurence I would suggest doing single squats, forward-backward sprints, burbee-pullups and going on the treadmill every week.",
            "muscle_gain": "For muscle gain, consume a diet high in protein, healthy fats, and complex carbs thus for breakfast have scrambles eggs, oatmeal and fruit, for lunch have a beef burger, white rise, broccoli and for dinner have salmon, quinoa, asaragys. Include strength training exercises like weight lifting, resistance training, and bodyweight exercises. Aim to work each muscle group twice a week thus at the gym thus at the gym do light cardio, barbell bench presses, incline dumbbell presses, bicep curls, leg curls, leg press, dumbbell lateranl rises.",
            "weight_loss": "To lose weight, focus on a diet low in refined carbs, sugars, and unhealthy fats. Include plenty of fruits, vegetables, and lean proteins thus for breakfast have tea and fruit, fo lunch have a beef burger and vegetables and for dinner have stir fried. Incorporate a mix of aerobic exercises and strength training thus at the gym do jumping jacks, burpees, use the starimaster "
        }

        self.recommendation_text.delete(1.0, END)
        self.recommendation_text.insert(END, recommendations[focus])

    def exit(self):
        self.window.quit()
        self.window.destroy()

if __name__ == "__main__":
    app = App()
