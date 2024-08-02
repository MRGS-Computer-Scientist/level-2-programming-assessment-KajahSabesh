from tkinter import *
from tkinter import messagebox  # Import messagebox for showing error messages
from datetime import datetime, timedelta
from PIL import Image, ImageTk
from os import path
import re

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

        self.build_main_page()  # Build the main page layout
        self.build_signup_page()  # Build the signup page layout

        self.workout_routines = {}
        self.current_date = datetime.now()

        self.window.mainloop()

    def build_main_page(self):
        """Build the main page layout with header, content, and navigation buttons."""
        self.header_frame = Frame(self.main_frame, background='black', height=100)
        self.header_frame.pack(fill=X, side='top')

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

        self.dirname = path.dirname(__file__)
        self.filename = path.join(self.dirname, 'images/logo.png')
        self.load_logo_image()

        self.content_frame = Frame(self.main_frame, background='black')
        self.content_frame.pack(fill=BOTH, expand=True)

        welcome_text = f"Hello, {self.signup_name.get()}!" if hasattr(self, 'signup_name') else "Hello!"
        self.welcome_label = Label(self.content_frame, bg='black', fg='white', text=welcome_text, font=("Helvetica", 14, "bold"))
        self.welcome_label.pack(pady=10)

        self.red_box1 = Label(self.content_frame, bg='red', text="Activities:", font=("Helvetica", 14, "bold"))
        self.red_box1.pack(pady=20, fill=BOTH, expand=True)

        self.red_box2 = Label(self.content_frame, bg='red', text="Calories Burnt:", font=("Helvetica", 14, "bold"))
        self.red_box2.pack(pady=20, fill=BOTH, expand=True)

        self.red_box3 = Label(self.content_frame, bg='red', text="BMI:", font=("Helvetica", 14, "bold"))
        self.red_box3.pack(pady=20, fill=BOTH, expand=True)

        self.signup_button = Button(self.content_frame, text="Get Started", bg='green', fg='white', command=self.show_signup_page, font=button_font)
        self.signup_button.pack(pady=10)

    def build_signup_page(self):
        """Build the signup page layout with input fields and submit button."""
        Label(self.signup_frame, text="Get Started", font=("Helvetica", 24, "bold"), bg='black', fg='white').pack(pady=20)

        self.signup_name = Entry(self.signup_frame, font=("Helvetica", 14))
        self.signup_name.pack(pady=10)
        self.signup_name.insert(0, "Username")

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

        Button(self.signup_frame, text="Submit", bg='green', fg='white', font=("Helvetica", 14, "bold"), command=self.calculate_calories).pack(pady=0)
        Button(self.signup_frame, text="Back to Home", bg='red', fg='white', command=self.show_main_page, font=("Helvetica", 14, "bold")).pack(pady=10)

    def show_main_page(self):
        """Show the main page and hide the signup page."""
        self.signup_frame.pack_forget()
        self.main_frame.pack(fill=BOTH, expand=True)

    def show_signup_page(self):
        """Show the signup page and hide the main page."""
        self.main_frame.pack_forget()
        self.signup_frame.pack(fill=BOTH, expand=True)

    def show_calendar_page(self):
        """Show the calendar page in a new window."""
        self.calendar_window = Toplevel(self.window)
        self.calendar_window.title("Calendar")
        self.calendar_window.geometry(f"375x850+{int((self.window.winfo_screenwidth() / 2) - (375 / 2))}+{int((self.window.winfo_screenheight() / 2) - (850 / 2))}")
        self.calendar_window.configure(background="black")

        self.calendar_window.protocol("WM_DELETE_WINDOW", self.confirm_calendar_close)

        Label(self.calendar_window, text="Calendar", font=("Helvetica", 24, "bold"), bg='black', fg='white').pack(pady=20)

        self.calendar_frame = Frame(self.calendar_window, bg='black')
        self.calendar_frame.pack(pady=10)

        self.prev_button = Button(self.calendar_frame, text="←", command=self.prev_day, bg='red', fg='black', font=("Helvetica", 14, "bold"))
        self.prev_button.grid(row=0, column=0, padx=20)

        self.date_label = Label(self.calendar_frame, text=self.current_date.strftime('%Y-%m-%d'), font=("Helvetica", 14), bg='black', fg='white')
        self.date_label.grid(row=0, column=1, padx=20)

        self.next_button = Button(self.calendar_frame, text="→", command=self.next_day, bg='red', fg='black', font=("Helvetica", 14, "bold"))
        self.next_button.grid(row=0, column=2, padx=20)

        Label(self.calendar_window, text="Enter your workout routine for the selected day below:", font=("Helvetica", 11), bg='black', fg='white').pack(pady=10)

        self.workout_text = Text(self.calendar_window, height=15, width=40, font=("Helvetica", 14), bg='white', wrap='word')
        self.workout_text.pack(pady=20)

        if self.current_date.strftime('%Y-%m-%d') in self.workout_routines:
            self.workout_text.insert(END, self.workout_routines[self.current_date.strftime('%Y-%m-%d')])

        Button(self.calendar_window, text="Save", bg='green', fg='white', command=self.save_workout, font=("Helvetica", 14, "bold")).pack(pady=10)
        Button(self.calendar_window, text="Close", bg='red', fg='white', command=self.confirm_calendar_close, font=("Helvetica", 14, "bold")).pack(pady=10)

    def show_diet_page(self):
        """Show the diet page in a new window."""
        self.diet_window = Toplevel(self.window)
        self.diet_window.title("Diet and Exercise")
        self.diet_window.geometry(f"375x850+{int((self.window.winfo_screenwidth() / 2) - (375 / 2))}+{int((self.window.winfo_screenheight() / 2) - (850 / 2))}")
        self.diet_window.configure(background="black")

        self.diet_window.protocol("WM_DELETE_WINDOW", self.confirm_diet_close)

        Label(self.diet_window, text="Diet and Exercise", font=("Helvetica", 24, "bold"), bg='black', fg='white').pack(pady=20)

        self.diet_frame = Frame(self.diet_window, bg='black')
        self.diet_frame.pack(pady=10)

        Label(self.diet_window, text="Enter your diet and exercise for the day below:", font=("Helvetica", 11), bg='black', fg='white').pack(pady=10)

        self.diet_text = Text(self.diet_window, height=15, width=40, font=("Helvetica", 14), bg='white', wrap='word')
        self.diet_text.pack(pady=20)

        if self.current_date.strftime('%Y-%m-%d') in self.workout_routines:
            self.diet_text.insert(END, self.workout_routines[self.current_date.strftime('%Y-%m-%d')])

        Button(self.diet_window, text="Save", bg='green', fg='white', command=self.save_diet, font=("Helvetica", 14, "bold")).pack(pady=10)
        Button(self.diet_window, text="Close", bg='red', fg='white', command=self.confirm_diet_close, font=("Helvetica", 14, "bold")).pack(pady=10)

    def exit(self):
        """Exit the application after confirmation."""
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.window.destroy()

    def load_logo_image(self):
        """Load and display the logo image in the header."""
        if path.isfile(self.filename):
            logo_image = Image.open(self.filename)
            logo_image = logo_image.resize((150, 150), Image.LANCZOS)
            logo_photo = ImageTk.PhotoImage(logo_image)
            self.logo_label = Label(self.header_frame, image=logo_photo, bg='black')
            self.logo_label.image = logo_photo
            self.logo_label.pack(pady=10)
        else:
            print(f"Error: File not found - {self.filename}")

    def calculate_calories(self):
        """Calculate the calories burned based on user's input and show the result."""
        weight = self.signup_weight.get()
        try:
            weight = float(weight)
            km_ran = self.signup_km_ran.get()
            km_ran = float(km_ran)
            calories_burned = self.calculate_calories_burned(weight, km_ran)
            messagebox.showinfo("Calories Burned", f"You have burned {calories_burned:.2f} calories.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numeric values for weight and kilometers ran.")

    def calculate_calories_burned(self, weight, km_ran):
        """Return the calories burned based on weight and kilometers ran."""
        MET = 9.8  # Metabolic Equivalent for running at 6 mph (approximately 9.8 METs)
        calories_per_minute = (MET * 3.5 * weight) / 200
        minutes_ran = (km_ran / 10) * 60  # Assuming 10 km/h speed
        return calories_per_minute * minutes_ran

    def confirm_calendar_close(self):
        """Confirm before closing the calendar window."""
        if messagebox.askokcancel("Close", "Are you sure you want to close the calendar?"):
            self.calendar_window.destroy()

    def confirm_diet_close(self):
        """Confirm before closing the diet window."""
        if messagebox.askokcancel("Close", "Are you sure you want to close the diet and exercise window?"):
            self.diet_window.destroy()

    def prev_day(self):
        """Show the previous day's date in the calendar."""
        self.current_date -= timedelta(days=1)
        self.update_calendar_date()

    def next_day(self):
        """Show the next day's date in the calendar."""
        self.current_date += timedelta(days=1)
        self.update_calendar_date()

    def update_calendar_date(self):
        """Update the date label and text area in the calendar window."""
        self.date_label.config(text=self.current_date.strftime('%Y-%m-%d'))
        self.workout_text.delete(1.0, END)
        if self.current_date.strftime('%Y-%m-%d') in self.workout_routines:
            self.workout_text.insert(END, self.workout_routines[self.current_date.strftime('%Y-%m-%d')])

    def save_workout(self):
        """Save the workout routine for the selected date."""
        self.workout_routines[self.current_date.strftime('%Y-%m-%d')] = self.workout_text.get(1.0, END).strip()
        messagebox.showinfo("Saved", "Your workout routine has been saved.")

    def save_diet(self):
        """Save the diet and exercise for the selected date."""
        self.workout_routines[self.current_date.strftime('%Y-%m-%d')] = self.diet_text.get(1.0, END).strip()
        messagebox.showinfo("Saved", "Your diet and exercise have been saved.")

if __name__ == "__main__":
    app = App()
