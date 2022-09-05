from tkinter import *
from tkcalendar import *

root = Tk()
root.title("Codemy.com Calendar Picker")
root.geometry("600x480")

cal = Calendar(root, selectmode="day", year=2021, month=9, day=4)
cal.pack(pady=20, fill="both", expand=True)

def grab_date():
    my_label.config(text="Today's date is " + cal.get_date())

my_button = Button(root, text="Get Date", command=grab_date)
my_button.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()
