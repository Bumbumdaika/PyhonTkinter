from gui import MainWindow
import ttkbootstrap as ttk
from pathlib import Path
import ttkbootstrap as ttk
from tkinter import *
import pandas as pd
from pandastable import Table
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from append import Append
# from previe import Previe
# Import module
from tkinter import *
 
# Create object
splash_root = Tk()
 


# Adjust size
splash_root.geometry("1280x720")
splash_root.title("Hollow Knight db")
splash_root.iconbitmap("C:/Users/Admin/Desktop/Python LAB tkinter/build/cource/hollowknight64.ico")

splash_root.image = PhotoImage(file ='C:/Users/Admin/Desktop/Python LAB tkinter/build/hk.png')
bg_logo=Label(splash_root, image=splash_root.image)
bg_logo.grid(row=0, column = 0)
# Set Label
splash_label = Label(splash_root, text="Hollow Knight", font=14, fg="#fff")
splash_label.config(font=("Courier", 44), background='#323551')
splash_label.grid(row=0, column = 0)

# main window function


def main():
    # destroy splash window
    splash_root.destroy()
    mw = MainWindow()


# Set Interval
splash_root.after(1500, main)

# Execute tkinter
mainloop()
