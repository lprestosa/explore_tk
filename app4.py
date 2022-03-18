import csv
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import tkinter.ttk as ttk

"""
In my CSV File , there are two columns only CountryCode,CountryName. 
My requirement is like read csv file values and display the values in table format with scrollbar option , 
  for each row , one button will display .
  When click this button ,it new popup window that display corresponding countryDetails based on the countryCode

Here is my Code below

In my Code, I can able read csv file and display all the values with scroll bar option and display one button for each row .

Now my question is like ,for example 100 rows in CSV file ,
it display 100 button for each row how to bind the corresponding button with CountryCode and call the function openpopup"""


root = tk.Tk()
root.title("My Application")
width = 980
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
container = ttk.Frame(root)
canvas = tk.Canvas(container)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)
canvas.create_window((250, 250), window=scrollable_frame, anchor="nw")
canvas.place(x=80, y=400, width=800, height=600)
canvas.configure(yscrollcommand=scrollbar.set)
container.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


def read_csvfile():
    filepath = filedialog.askopenfilename(title="Open file")
    with open(filepath) as f:
        reader = csv.DictReader(f, delimiter=',')
        i = 0
        tk.Label(scrollable_frame, text="Country Code").grid(row=i, column=1)
        tk.Label(scrollable_frame, text="Country Name").grid(row=i, column=2)

        for row in reader:
            i = i + 1
            Countrycode = row['Country Code']
            Countryname = row['Country Name']
            tk.Label(scrollable_frame, text=Countrycode).grid(row=i, column=1)
            tk.Label(scrollable_frame, text=Countryname).grid(row=i, column=2)
            ttk.Button(scrollable_frame, text="ViewCountryDetails " + str(i)).grid(row=i, column=3)


button = Button(root, text='Read CSVFile', command=read_csvfile)
button.place(x=40, y=40)

root.mainloop()