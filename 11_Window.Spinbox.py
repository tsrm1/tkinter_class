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
        
        self.choice = StringVar()
        self.spin_var = StringVar()
        self.spin_value = Spinbox(self.root, values=("One", "Two", "Three"))

    def draw_widgets(self):
        Spinbox(self.root).pack(anchor=NW)

        Spinbox(self.root, width=30, bg='black', fg='white', buttonbackground='blue').pack(anchor=NW)

        Spinbox(self.root, relief=RAISED, bd=3, buttonuprelief=SUNKEN, buttondownrelief=RAISED).pack(anchor=NW)

        txt = StringVar(value='DEFAULT TEXT')
        Spinbox(self.root, textvariable=txt, font=("Calibri", 12), justify=CENTER, selectbackground="yellow", selectforeground="red").pack(anchor=NW)

        Spinbox(self.root, from_=2, to=10, increment=2, wrap=True, textvariable=self.choice, command=self.my_commmand).pack(anchor=NW)
        # from_=2       - начальное значение
        # to=10         - конечное значение
        # increment=2   - шаг изменения
        # wrap=True     - цикличсекий перебор значений, при достижении макс.позиции, переходим в начало


        Spinbox(self.root, values=('one', 2, '3', 'four'), state='readonly', textvariable=self.spin_var).pack(anchor=NW)
        # значения могут быть любые, они всё равно будут переведены в строковые значения
        # state='readonly' - запрет на ввод пользователем своих значений -> серый фон
        # textvariable=self.spin_value - привязываем к Spinbox текстовую переменную

        Button(self.root, text="Get value1", width=10, command=self.get_spin_var_value).pack(anchor=NW, padx=10)


        self.spin_value.pack(anchor=NW)


        Button(self.root, text="Get value2", width=10, command=self.get_spin_value).pack(anchor=NW, padx=10)
        Button(self.root, text="Quit", width=10, command=self.exit).pack(anchor=NW, padx=10)
    

    def my_commmand(self):                                              # получаем значение через переменную
        choice = self.choice.get()
        messagebox.showinfo("Info", f'Got value: {choice}')

    def get_spin_var_value(self):                                       # получаем значение через переменную
        choice = self.spin_var.get()
        messagebox.showinfo("Info", f'Got value: {choice}')

    def get_spin_value(self):                                           # получаем значение напрямую с виджета
        choice = self.spin_value.get()
        messagebox.showinfo("Info", f'Got value: {choice}')


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