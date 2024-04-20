# https://www.youtube.com/watch?v=2Ye9UzuthZc

from tkinter import *
from tkinter import messagebox


GRAY = 0
YELLOW = 1
ORANGE = 2
RED = 3

class Window:
    def __init__(self, width, height, title="MyWindow", resizable=(True, True), icon="ico/favicon.ico") -> None:
        self.root = Tk()                                # Инициалиция окна
        self.root.title(title)                          # название окна
        self.root.geometry(f"{width}x{height}+100+100") # "Ширина x Высота + Смещение по X + Смещение по Y"
        # self.root.minsize(400,300)                      # минимальные размеры: ширина - 200, высота - 150
        self.root.resizable(resizable[0], resizable[1]) # изменение окна по осям              
        if icon !="":
            self.root.iconbitmap(icon)                  # установка иконки для окна
        
        self.choice = IntVar(value=0)
        self.info = Label(self.root)




    def draw_widgets(self):
        
        Radiobutton(self.root, text='GRAY', variable=self.choice, value=GRAY, indicatoron=0, command=lambda: self.show_info("gray")).pack(anchor=NW, padx=10)
        Radiobutton(self.root, text='YELLOW', variable=self.choice, value=YELLOW, indicatoron=0, command=lambda: self.show_info("yellow")).pack(anchor=NW, padx=10)
        Radiobutton(self.root, text='ORANGE', variable=self.choice, value=ORANGE, indicatoron=0, command=lambda: self.show_info("orange")).pack(anchor=NW, padx=10)
        Radiobutton(self.root, text='RED', variable=self.choice, value=RED, indicatoron=0, command=lambda: self.show_info("red")).pack(anchor=NW, padx=10)
        self.info.pack(anchor=NW, padx=10)

        Button(self.root, text="Save", width=10, command=self.choice_info).pack(anchor=NW, padx=10)
        Button(self.root, text="Quit", width=10, command=self.exit).pack(anchor=NW, padx=10)


    def show_info(self, color):
        if color == 'gray':
            self.root.configure(bg='gray')
            self.info.configure(text="Color name: gray, Hex: #bebebe, RGB: rgb(190,190,190", bg='black', fg='gray')

        elif color == 'yellow':
            self.root.configure(bg="yellow")
            self.info.configure(text="Color name: yellow, Hex: #ffff00, RGB: rgb(255,255,0)", bg='green', fg='yellow')

        elif color == 'orange':
            self.root.configure(bg="orange")
            self.info.configure(text="Color name: orange, Hex: #ffa500, RGB: rgb(255,165,0)", bg='cyan', fg='orange')

        elif color == 'red':
            self.root.configure(bg="red")
            self.info.configure(text="Color name: red, Hex: #ff0000, RGB: rgb(255,0,0)", bg='yellow', fg='red')


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