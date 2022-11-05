from tkinter import *
from tkinter import messagebox
from time import sleep

root = Tk()

# Pop Up
def isup():
    messagebox.showinfo("Hey!", "Time is up :)")

# Time
def timer():
    hours = he.get()
    if hours.isnumeric() and hours is not None:
        hours = int(hours)*60*60
    else:
        hours = 0
    mins = me.get()
    if mins.isnumeric() and mins is not None:
        mins = int(mins)*60
    else:
        mins = 0
    sec = se.get()
    if sec.isnumeric() and sec is not None:
        sec = int(sec)
    else:
        sec = 0

    tot = sec + mins + hours

    sleep(tot)

    isup()

# Window Size
root.geometry("400x150")

# Disable Resize
root.resizable(False, False)

# Title
root.title("Timer")

# Hours
Label(root, text="Hours: ").grid(row=0, column=0, pady=15, padx=20)
he = Entry(root, width=25)
he.grid(row=0, column=1)

# Minutes
Label(root, text="Minutes: ").grid(row=1, column=0, pady=15, padx=20)
me = Entry(root, width=25)
me.grid(row=1, column=1)

# Seconds
Label(root, text="Seconds: ").grid(row=2, column=0, pady=15, padx=20)
se = Entry(root, width=25)
se.grid(row=2, column=1)

# Button
btn = Button(root, text="Time", command=timer).grid(row=1, column=2, padx=30)

mainloop()
