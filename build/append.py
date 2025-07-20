import tkinter as tk
import ttkbootstrap as ttk
from tkinter import *
import pandas as pd
class Append(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Hollow Knight db append")
        self.geometry("600x400")
        self.configure(bg ="#323551")
        self.iconbitmap("C:/Users/Admin/Desktop/Python LAB tkinter/build/cource/hollowknight64.ico")

        notebook = ttk.Notebook(self,bootstyle='success')
        notebook.pack(pady=5)
        
        def addenemy():
            df1 = pd.DataFrame({'Name': [textbox_1.get()], 'Health': [textbox_2.get()]})
            df2 = pd.read_excel('C:/Users/Admin/Desktop/Python LAB tkinter/build/enemies.xlsx')
            df = pd.concat([df2, df1])
            df.to_excel('C:/Users/Admin/Desktop/Python LAB tkinter/build/enemies.xlsx', index = False)
            # return df
        
        def addboss():
            df1 = pd.DataFrame({'Name': [textbox_3.get()], 'Health': [textbox_4.get()]})
            df2 = pd.read_excel('C:/Users/Admin/Desktop/Python LAB tkinter/build/boss.xlsx')
            df = pd.concat([df2, df1])
            df.to_excel('C:/Users/Admin/Desktop/Python LAB tkinter/build/boss.xlsx', index = False )
            # return df


        tab1 = ttk.Frame(notebook, height=600, width=400)

        label_1 = ttk.Label(tab1,bootstyle='success', text="Name")
        label_1.pack(pady=20)

        textbox_1=ttk.Entry(tab1,bootstyle='success',)
        textbox_1.pack(pady=20)
        
        label_2 = ttk.Label(tab1,bootstyle='success', text="Health")
        label_2.pack(pady=20)

        textbox_2=ttk.Entry(tab1,bootstyle='success',)
        textbox_2.pack(pady=20)

        btn1 = ttk.Button(tab1,bootstyle='success', text="Add Enemies", command=addenemy)
        btn1.pack(pady=20)
        


        tab2 = ttk.Frame(notebook)

        label_3 = ttk.Label(tab2,bootstyle='success', text="Name")
        label_3.pack(pady=20)

        textbox_3=ttk.Entry(tab2,bootstyle='success',)
        textbox_3.pack(pady=20)
        
        label_4 = ttk.Label(tab2,bootstyle='success', text="Health")
        label_4.pack(pady=20)

        textbox_4=ttk.Entry(tab2,bootstyle='success',)
        textbox_4.pack(pady=20)

        btn3 = ttk.Button(tab2,bootstyle='success', text="Add Boss", command=addboss)
        btn3.pack(pady=20)


        btn2 = ttk.Button(self,bootstyle='success', text = "Cancel", command=self.destroy)
        btn2.pack(pady=20)

        
        notebook.add(tab1,text='add Enemies')
        notebook.add(tab2,text='add Boss')

        self.mainloop()