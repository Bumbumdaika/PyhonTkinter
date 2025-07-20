from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import ttkbootstrap as ttk
from artem_tarasovskii_geniy import Vakansii
from pandastable import Table
import pandas as pd

class MainWindow(ttk.Window):
    def __init__(self):
        super().__init__()

        self.themename = 'minty'
        self.title("Анализ вакансий")
        self.geometry("1440x1024")
        self.resizable(False,False)

        self.canvas = Canvas(
                            self,
                            bg = "#FFFFFF",
                            height = 1024,
                            width = 1440,
                            bd = 0,
                            highlightthickness = 0,
                            relief = "ridge")
        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
                51.0,
                57.0,
                1058.0,
                124.0,
                fill="#D9D9D9",
                outline="")

        self.combobox_prof = ttk.Combobox(self,bootstyle='success',values=['Программист','Аналитик', 'Дворник', 'Разработчик игр'],
                                        font=("Inter", 24 * -1))
        self.combobox_prof.place(x=790,y=72, width=220)

        def click_bind(e):
            pass
        self.combobox_prof.bind("<<ComboboxSelected>>",click_bind)	

        self.canvas.create_text(
            554.0,
            71.0,
            anchor="nw",
            text="ПРОФЕССИЯ",
            fill="#000000",
            font=("Inter", 32 * -1)
        )

        self.combobox_region = ttk.Combobox(self,bootstyle='success',values=['Приморский край','Хабаровский край'],
                                        font=("Inter", 24 * -1))
        self.combobox_region.place(x=292,y=72, width=220)


        self.canvas.create_text(
            96.0,
            71.0,
            anchor="nw",
            text="РЕГИОН",
            fill="#000000",
            font=("Inter", 32 * -1)
        )
        b1 = PhotoImage(file="C:/Users/Admin/Desktop/Python LAB tkinter/hh_dash/button_1.png")
        self.button_1 = Button(
            image=b1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(
            x=1113.0,
            y=306.0,
            width=262.0,
            height=63.0
        )
        def getvakansii():
            Vakansii()
        b2 = PhotoImage(file="C:/Users/Admin/Desktop/Python LAB tkinter/hh_dash/button_2.png")
        self.button_2 = Button(
            image=b2,
            borderwidth=0,
            highlightthickness=0,
            command= getvakansii,
            relief="flat"
        )
        self.button_2.place(
            x=1113.0,
            y=185.0,
            width=262.0,
            height=63.0
        )

        self.notebook = ttk.Notebook(self)

        tab1 = ttk.Frame(self.notebook)
        df = pd.read_excel('C:/Users/Admin/Desktop/Python LAB tkinter/hh_dash/vacc.xlsx')

        

        table = Table(tab1,dataframe=df)
        table.show()

        
        tab2 = ttk.Frame(self.notebook)

        self.notebook.add(tab1,text='Данные')
        self.notebook.add(tab2,text='Дашборд')

        self.notebook.place(x=51,y=160,width=1007,height=776)

        self.mainloop()
