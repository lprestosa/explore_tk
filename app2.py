import tkinter as tk
import easygui
import pandas as pd
from time import strftime
from app2_flight_bot import Flight_Bot





window = tk.Tk() # you may also see it named as "root" in other sources

window.title("WINDOW TITLE") # self explanatory!
#window.geometry("600x600") # size of the window when it opens
window.minsize(width=600, height=600) # you can define the minimum size of the window like this
window.resizable(width="true", height="true") # change to false if you want to prevent resizing

# Put it simply: StringVar() allows you to easily track tkinter variables and see if they were read, changed, etc
# check resources here for more details: http://effbot.org/tkinterbook/variable.htm
from_city1 = tk.StringVar()
to_city1 = tk.StringVar()
departure_date1 = tk.StringVar()
return_date1 = tk.StringVar()

def caps_from(event):
    """Forces the input FROM to be upper case and less than 4 characters"""
    from_city1.set(from_city1.get().upper())
    if len(from_city1.get()) > 3: from_city1.set(from_city1.get()[:3])


def caps_to(event):
    """Forces the input TO to be upper case and less than 4 characters"""
    to_city1.set(to_city1.get().upper())
    if len(to_city1.get()) > 3: to_city1.set(to_city1.get()[:3])


def close_app():
    window.destroy()


def run_app():
    print('run')

# WIDGETS
# three frames on top of each other
frame_header = tk.Frame(window, borderwidth=2, pady=2)
center_frame = tk.Frame(window, borderwidth=2, pady=5)
bottom_frame = tk.Frame(window, borderwidth=2, pady=5)
frame_header.grid(row=0, column=0)
center_frame.grid(row=1, column=0)
bottom_frame.grid(row=2, column=0)

# label header to be placed in the frame_header
header = tk.Label(frame_header, text = "FRAME HEADER", bg='grey', fg='black', height='3', width='50', font=("Helvetica 16 bold"))
# inside the grid of frame_header, place it in the position 0,0
header.grid(row=0, column=0)

# two additional frames go inside the center_frame
frame_main_1 = tk.Frame(center_frame, borderwidth=2, relief='sunken')
frame_main_2 = tk.Frame(center_frame, borderwidth=2, relief='sunken')

# and populate them with the labels referring to the inputs we want from the user
from_city = tk.Label(frame_main_1, text = "FROM: ")
to_city = tk.Label(frame_main_2, text = "TO:      ")
departure_date = tk.Label(frame_main_1, text = "    DEPARTURE DATE:")
return_date = tk.Label(frame_main_2, text = "     RETURN DATE:")

# Put it simply: StringVar() allows you to easily track tkinter variables and see if they were read, changed, etc
# check resources here for more details: http://effbot.org/tkinterbook/variable.htm
from_city1 = tk.StringVar()
to_city1 = tk.StringVar()
departure_date1 = tk.StringVar()
return_date1 = tk.StringVar()

## creating the entries for the user input, FROM, TO and dates
from_city_entry = tk.Entry(frame_main_1, textvariable = from_city1, width=4)
from_city_entry.bind("<KeyRelease>", caps_from) # everytime a key is released, it runs the caps_from function on the cell

to_city_entry = tk.Entry(frame_main_2, textvariable = to_city1, width=4)
to_city_entry.bind("<KeyRelease>", caps_to) # everytime a key is released, it runs the caps_to function on the cell

departure_date_entry = tk.Entry(frame_main_1, textvariable = departure_date1, width=12)
return_date_entry = tk.Entry(frame_main_2, textvariable = return_date1, width=12)

# and we pack the two frames in the center_frame and then the elements inside them
frame_main_1.pack(fill='x', pady=2)
frame_main_2.pack(fill='x',pady=2)
#
# the order which we pack the items is important
from_city.pack(side='left')
from_city_entry.pack(side='left', padx=1)
departure_date.pack(side='left', padx=5)
departure_date_entry.pack(side='left')
to_city.pack(side='left')
to_city_entry.pack(side='left', padx=1)
return_date_entry.pack(side='right')
return_date.pack(side='right', padx=5)




def caps_from(event):
    """Forces the input FROM to be upper case and less than 4 characters"""
    from_city1.set(from_city1.get().upper())
    if len(from_city1.get()) > 3: from_city1.set(from_city1.get()[:3])


def caps_to(event):
    """Forces the input TO to be upper case and less than 4 characters"""
    to_city1.set(to_city1.get().upper())
    if len(to_city1.get()) > 3: to_city1.set(to_city1.get()[:3])


def close_app():
    window.destroy()


def run_app():
    print('getting user inputs')
    user_city_from = str(from_city_entry.get())
    user_city_to = str(to_city_entry.get())
    user_date_depart = str(departure_date_entry.get())
    user_date_return = str(return_date_entry.get())

    print('starting Chrome')
    bot = Flight_Bot()
    bot.start_kayak(user_city_from, user_city_to, user_date_depart, user_date_return)

# a proper app needs some buttons too!
button_run = tk.Button(bottom_frame, text="Start", command=run_app, bg='dark green', fg='white', relief='raised', width=10, font=('Helvetica 9 bold'))
button_run.grid(column=0, row=0, sticky='w', padx=100, pady=2)

button_close = tk.Button(bottom_frame, text="Exit", command=close_app, bg='dark red', fg='white', relief='raised', width=10, font=('Helvetica 9'))
button_close.grid(column=1, row=0, sticky='e', padx=100, pady=2)



window.mainloop()