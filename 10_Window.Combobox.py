# https://www.youtube.com/watch?v=2Ye9UzuthZc

from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox


class Window:
    def __init__(self, width, height, title="MyWindow", resizable=(True, True), icon="ico/favicon.ico") -> None:
        self.root = Tk()                                # Инициалиция окна
        self.root.title(title)                          # название окна
        self.root.geometry(f"{width}x{height}+100+100") # "Ширина x Высота + Смещение по X + Смещение по Y"
        # self.root.minsize(400,300)                      # минимальные размеры: ширина - 200, высота - 150
        self.root.resizable(resizable[0], resizable[1]) # изменение окна по осям              
        if icon !="":
            self.root.iconbitmap(icon)                  # установка иконки для окна
        

        # box_text = StringVar(value="default")
        # self.numbers = Combobox(self.root, value=(3, 6, 9, 12, 15), state="readonly", textvariable=box_text)
        self.numbers = Combobox(self.root, value=(3, 6, 9, 12, 15), state="readonly")
        # state="readonly" - пользователь не может вводить текст
        # state="normal" - пользователь может вводить свой текст, установлен по умолчанию
        # state="disabled" - виджет становиться не активным, ничего нельзя выбрать
         

    def draw_widgets(self):
        # Самый простой Combobox
        Combobox(self.root, values=(1, 3, 5)).pack(anchor=NW)
        
        # С использованием переменной, чтобы был доступ к Combobox в будущем
        c = Combobox(self.root, values=(2, 4, 6))
        c.current(1)        # установка текущего значения, указываем индекс в списке
        c.pack(anchor=NW)

        # Текстовый Combobox, используется выравнивание результата в строке
        Combobox(self.root, values=('one', 'two', 'three'), justify=CENTER).pack(anchor=NW)

        # Установка state (normal, readonly, disabled) для Combobox
        self.numbers.pack(anchor=NW)

        # Устанавливаем на Combobox отслеживание событий (<<ComboboxSelected>> - изменения)
        # и вызов функции, при изменении выбора
        self.numbers.bind("<<ComboboxSelected>>", self.on_changed)

        Button(self.root, text="Get", width=10, command=self.get_number).pack(anchor=NW, padx=10)
        Button(self.root, text="Quit", width=10, command=self.exit).pack(anchor=NW, padx=10)

    def on_changed(self, event):
        value = self.numbers.get()          # возвращает значение
        index = self.numbers.current()      # возвращает индекс/позицию значения из/в списка
        messagebox.showinfo("Get info", f'Index:{index}, value: {value}')

    def get_number(self):
        value = self.numbers.get()          # возвращает значение
        index = self.numbers.current()      # возвращает индекс/позицию значения из/в списка
        # index = -1 - пользователь ничего не выбрал
        messagebox.showinfo("Get info", f'Index:{index}, value: {value}')

    def exit(self):
        choice = messagebox.askyesno("Quit", "Do you want to quit?")            # Да/Нет = True/False
        # choice = messagebox.askokcancel("Quit", "Do you want to quit?")       # ОК/Отмена = True/False
        # choice = messagebox.askretrycancel("Quit", "Do you want to quit?")    # Повтор/Отмена = True/False
        # choice = messagebox.askyesnocancel("Quit", "Do you want to quit?")    # Да/Нет/Отмена = True/False/None
        
        print(f'Quit={choice}')
        if choice:
            self.root.destroy()


    # def choice_info(self):
    #     choice = self.choice.get()
    #     messagebox.showinfo("Info", f"Choice = {choice}")

    def run(self):
        self.draw_widgets()             # прорисовка виджетов в окне root
        self.root.mainloop()


if __name__ == "__main__":
    window = Window(300, 350, "TestWindow", resizable=(False, False))
    window.run()