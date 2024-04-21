# https://www.youtube.com/watch?v=2Ye9UzuthZc

from tkinter import *
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
        
        self.parameters = (("red", IntVar()), ("green", IntVar()), ("blue", IntVar()), ("white", IntVar()))

        self.btn1 = Checkbutton(self.root, text="Btn1", indicatoron=0)
        self.btn2 = Checkbutton(self.root, text="Btn2", indicatoron=0)
        self.btn3 = Checkbutton(self.root, text="Btn3", indicatoron=0)
        self.btn4 = Checkbutton(self.root, text="Btn4", indicatoron=0)

        self.buttons = (self.btn1, self.btn2, self.btn3, self.btn4)
        
        
    def draw_widgets(self):
        Label(self.root, text="Choose colors").pack(anchor=NW)

        for name, var in self.parameters:
            Checkbutton(self.root, text=name, variable=var).pack(anchor=NW)

        Checkbutton(self.root, text="Command", command=self.change_state).pack(anchor=NW)

        # Checkbutton(self.root, text="Btn1", indicatoron=0).pack(anchor=NW)
        # Checkbutton(self.root, text="Btn2", indicatoron=0).pack(anchor=NW)
        # Checkbutton(self.root, text="Btn3", indicatoron=0).pack(anchor=NW)
        # Checkbutton(self.root, text="Btn4", indicatoron=0).pack(anchor=NW)

        for btn in self.buttons:
            btn.pack(anchor=NW)
        # self.btn1.pack(anchor=NW)
        # self.btn2.pack(anchor=NW)
        # self.btn3.pack(anchor=NW)
        # self.btn4.pack(anchor=NW)


        Button(self.root, text="Change Btn", width=10, command=self.invert_btn_state).pack(anchor=NW, padx=10)
        Button(self.root, text="Save", width=10, command=self.show_parameters).pack(anchor=NW, padx=10)
        Button(self.root, text="Quit", width=10, command=self.exit).pack(anchor=NW, padx=10)

    def invert_btn_state(self):
        for btn in self.buttons:
            btn.toggle()            # изменить статус флажка на противоположный
            # btn.select()            # выделить флажок
            # btn.deselect()          # убрать выделение флажка
            # btn.invoke()            # вызвать команду, которая была привязана к Checkbutton, аргумент command=...
            




    def change_state(self):
        messagebox.showinfo("Command", "Check button changed state")

    def show_parameters(self):
        state = ('inaktive', 'active')
        text = ''
        
        for name, var in self.parameters:
            text += f'{name} is {state[var.get()]}\n'
        messagebox.showinfo("Parameters", text)
        


    def exit(self):
        choice = messagebox.askyesno("Quit", "Do you want to quit?")            # Да/Нет = True/False
        # choice = messagebox.askokcancel("Quit", "Do you want to quit?")       # ОК/Отмена = True/False
        # choice = messagebox.askretrycancel("Quit", "Do you want to quit?")    # Повтор/Отмена = True/False
        # choice = messagebox.askyesnocancel("Quit", "Do you want to quit?")    # Да/Нет/Отмена = True/False/None
        
        print(f'Quit={choice}')
        if choice:
            self.root.destroy()


    def run(self):
        self.draw_widgets()             # прорисовка виджетов в окне root
        self.root.mainloop()


if __name__ == "__main__":
    window = Window(300, 350, "TestWindow", resizable=(False, False))
    window.run()