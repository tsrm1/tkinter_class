# https://www.youtube.com/watch?v=LMsg0poyrHQ

from tkinter import *
from child_window import ChildWindow

class Window:
    def __init__(self, width, height, title="MyWindow", resizable=(True, True), icon="ico/favicon.ico") -> None:
        self.root = Tk()                                # Инициалиция окна
        self.root.title(title)                          # название окна
        self.root.geometry(f"{width}x{height}+100+100") # "Ширина x Высота + Смещение по X + Смещение по Y"
        # self.root.minsize(400,300)                      # минимальные размеры: ширина - 200, высота - 150
        self.root.resizable(resizable[0], resizable[1]) # изменение окна по осям              
        if icon !="":
            self.root.iconbitmap(icon)                  # установка иконки для окна
    
        self.label1 = Label(self.root, text="Hello world!", bg="yellow", relief=RIDGE, wraplength=70, font="Consolas 15")
        # bg="yellow", цвет фона
        # relief=RIDGE, вид рельефа/рамка
        # wraplength=70, длина строки в px
        # font="Consolas 15", шрифт и размер
        
        # formats: .pgm, .ppm, .gif, .png
        self.face_image = PhotoImage(file="./ico/icon2.png")
        self.label2 = Label(self.root, image=self.face_image)
        # self.label2.image = self.face_image
        
    def draw_widgets(self):
        # self.label1.pack(anchor=NW)
        self.label1.pack()
        self.label2.pack()

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    
    def create_child(self, width, height, title="ChildWindow", resizable=(True, True), icon="ico/favicon.ico") -> None:
        ChildWindow(self.root, width, height, title, resizable, icon)


if __name__ == "__main__":
    window = Window(600, 400, "TestWindow")
    window.create_child(300, 200)
    window.run()