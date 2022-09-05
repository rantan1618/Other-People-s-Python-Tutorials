import tkinter as tk
import time as tm

class DigitalClock:
    def __init__(self, the_window):
        self.the_window = the_window
        self.the_window.title("Digital Clock")
        self.clock_display()
        self.display_time()

    def clock_display(self):
        self.clock_label=tk.Label(self.the_window,font='arial 80',bg='black',fg='red')
        self.clock_label.grid(row=0,column=0)

    def display_time(self):
        self.current_time = tm.strftime('%H:%M:%S')
        self.clock_label['text'] = self.current_time
        self.the_window.after(200,self.display_time)

my_window = tk.Tk()
my_digital_clock = DigitalClock(my_window)
my_window.mainloop()