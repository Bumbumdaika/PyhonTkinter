import pandas as pd
from tkinter import *
from tkcalendar import Calendar, DateEntry
class App:
    def __init__(self, root):
        self.root = root
        self.init_ui()
        def init_ui(self):
        # Создаем таблицу
             self.table = pd.DataFrame()
             self.df = pd.read_csv('data.csv')
             self.data = self.df.values
             self.columns = self.df['Col1'].tolist()
        # Задаем заголовки таблицы
        self.header = [''] * len(self.columns)
        for i in range(len(self.headers)):
            self.header[i] = Label(text=self.columns[i], font=("Helvetica", 12))
            self.header[i].pack(side=LEFT)
            # Добавляем строки таблицы
        for row in self.data:
            row = list(row)
        if len(row) == len(self.header):
            self.line = Listbox(self.root, height=20, width=50, bg='white')
            self.line.insert(END, ' '.join(row))
            self.line.pack(side=RIGHT)
        # Устанавливаем размеры таблицы
        width = max(map(lambda x: len(x), self.headers)) + 20
        height = len(self.rows)
        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=True, padx=5, pady=5)
        self.pack()
        # Запоминаем координаты верхнего левого угла окна
        x1 = self.app_layout['text'].winfo_rootx()
        y1 = self.app_layout['text'].winfo_rooty()
        # Обработчик события закрытия окна
        def close_window_append(self, widget):
            widget.destroy()
        # Закрываем окно ввода данных после добавления строки
        def update_app_window(self, window):
            window.update()
        window['text'].destroy()
        return
        # Добавляем новую строку в таблицу
        def add_row(self):
            row = {}
        for col in self.columns:
            row[col] = self.line.get(0, END)
        row.update(self.df[self.df.columns.to_list()].values[len(self.lines)-1])
        self.lines.append(row)
        self.update()
        # Обновляем содержимое таблицы
        def update(self):
            data = []
        for line in self.lines:
            data.extend(line)
        df = pd.DataFrame(data, columns=self.columns, index=pd.Index(range(len(data))))
        self.table.append(df)
        print(f'Table updated with new data')
        # Класс для создания окна ввода данных
        class app_window:
            def __init__(self, parent):
                super().__init__()
        self.parent = parent
        self.__init_app_layout()
        def show_app_window(self):
            self.app = App(self)
        self.geometry('300x150')
        def resizable(self, master=None, x=0, y=0):
            pass
        def geometry(self, w='300', h='150'):
            master.geometry(f'{w}x{h}')
        def size(self, master):
            w = master.winfo_width()
            h = master.winfo_height()
        return w, h
        def destroy(self):
            self.master.destroy()
        # Создаем окно для создания таблицы
        class window:
            def __init__(self, master, app):
                super(window, self).__init__(master)
        app.lines = []
        # Добавление кнопок для добавления и обновления таблицы
        layout = {'text': Text(self)}
        self.buttons = {}
        self.add_button = Button(layout, text='Add row', command=app.add_row)
        layout['text'].pack()
        layout['add'].pack(padx=10, pady=10)
        self.layout = layout
        self.text = Text(self)
        # Установка размеров окна
        self.w = 300
        self.h = 150
        # Реакция на закрытие окна
        def close(self, *args):
            app.close_window_update(self)
        return 'break'
        self._bind('WM_DELETE_WINDOW', close)
        return

nw = App()