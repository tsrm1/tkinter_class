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
        
        self.milk_var = IntVar()
        self.bread_var = IntVar()

        



    def draw_widgets(self):
        Label(self.root, text="Shopping bag").pack(anchor=NW)
        Checkbutton(self.root, text="Milk", variable=self.milk_var).pack(anchor=NW)
        Checkbutton(self.root, text="Bread", variable=self.bread_var).pack(anchor=NW)


        Button(self.root, text="Check", width=10, command=self.check_bag).pack(anchor=NW, padx=10)
        Button(self.root, text="Quit", width=10, command=self.exit).pack(anchor=NW, padx=10)

    def check_bag(self):
        text=''
        if self.milk_var.get():
            text += "You've bought milk\n"
        else: 
            text += "You need to buy milk\n"
        if self.bread_var.get():
            text += "You've bought bread\n"
        else: 
            text += "You need to buy bread\n"
        messagebox.showinfo("Bag", text)
        


    def exit(self):
        choice = messagebox.askyesno("Quit", "Do you want to quit?")            # Да/Нет = True/False
        # choice = messagebox.askokcancel("Quit", "Do you want to quit?")       # ОК/Отмена = True/False
        # choice = messagebox.askretrycancel("Quit", "Do you want to quit?")    # Повтор/Отмена = True/False
        # choice = messagebox.askyesnocancel("Quit", "Do you want to quit?")    # Да/Нет/Отмена = True/False/None
        
        print(f'Quit={choice}')
        if choice:
            self.root.destroy()


    def choice_info(self):
        choice = self.choice.get()
        messagebox.showinfo("Info", f"Choice = {choice}")

    def run(self):
        self.draw_widgets()             # прорисовка виджетов в окне root
        self.root.mainloop()


if __name__ == "__main__":
    window = Window(300, 300, "TestWindow", resizable=(False, False))
    window.run()