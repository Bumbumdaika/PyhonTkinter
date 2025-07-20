import ttkbootstrap as ttk
from hh import get_hh_df
import pandas as pd

class Vakansii(ttk.Window):
    def __init__(self):
        super().__init__()

        self.themename = 'minty'
        self.title("Сбор вакансий")
        self.geometry("400x400")
        self.resizable(False,False)
        self.combobox_prof = ttk.Combobox(self,bootstyle='success',values=['Программист','Аналитик', 'Дворник', 'Разработчик игр'],
                                        font=("Inter", 24 * -1))
        self.combobox_prof.pack(pady=20)
        def getvac():
            url = 'https://api.hh.ru/vacancies'
            params = {
            'text': f'NAME:{self.combobox_prof.get()}',
            'area': 22,
            'page':0,
            'per_page':100
            }
            df=get_hh_df(params)
            try:
                vac=pd.read_excel("vacc.xlsx")
                for index, row in df.iterrows():
                    vac.loc[len(vac)]=[row['name'],row['salary_from'],row['salary_to'],row['company']]
                vac.to_excel("vacc.xlsx",index=False)    
            except:
                df.to_excel("vacc.xlsx",index=False)
        
        self.Knopka=ttk.Button(self,bootstyle='success',command=getvac,text="собрать вакансии")
        self.Knopka.pack(pady=20)
        self.mainloop()


