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
    
        # self.label1 = Label(self.root, text="Hello world!", bg="yellow", relief=RIDGE, wraplength=70, font="Consolas 15")
        # # bg="yellow", цвет фона
        # # relief=RIDGE, вид рельефа/рамка
        # # wraplength=70, длина строки в px
        # # font="Consolas 15", шрифт и размер
        
        # # formats: .pgm, .ppm, .gif, .png
        # self.face_image = PhotoImage(file="./ico/icon2.png")
        # self.label2 = Label(self.root, image=self.face_image)
        # # self.label2.image = self.face_image
        
    def draw_widgets(self):
        Label(self.root, width=30, height=2, bg='red', text="First").place(x=10, y=10)
        Label(self.root, width=30, height=2, bg='orange', text="Second").place(x=30, y=46)
        Label(self.root, width=30, height=2, bg='yellow', text="Third").place(x=50, y=82)
        Label(self.root, width=30, height=2, bg='green', text="Fourth").place(x=70, y=118, width=100, height=50)

        Label(self.root, width=30, height=2, bg='red', text="Fiveth").place(relx=0.4, rely=0.4)
        Label(self.root, width=30, height=2, bg='orange', text="Sixth").place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.1)
        # Label(self.root, width=30, height=2, bg='yellow', text="Third").place(x=50, y=82)
        # Label(self.root, width=30, height=2, bg='green', text="Fourth").place(x=70, y=118)


    def draw_widgets_in_frames(self):
        label1 = Label(self.root, width=30, height=2, bg='red', text="First")
        label2 = Label(self.root, width=30, height=2, bg='orange', text="Second")
        # label3 = Label(self.root, width=30, height=2, bg='yellow', text="Third")
        # label4 = Label(self.root, width=30, height=2, bg='green', text="Fourth")

        label1.place(x=10, y=10)                # координата (x=10, y=10) верхнего левого угла виджета в окне root
        label2.place(in_=label1, x=10, y=10)    # координата (x=10, y=10) верхнего левого угла виджета в окне виджета label1



    def run(self):
        # self.draw_widgets()             # прорисовка виджетов в окне root
        self.draw_widgets_in_frames()   # прорисовка виджетов в рамках, которые находяться в окне root
        self.root.mainloop()

    
    def create_child(self, width, height, title="ChildWindow", resizable=(True, True), icon="ico/favicon.ico") -> None:
        ChildWindow(self.root, width, height, title, resizable, icon)


if __name__ == "__main__":
    window = Window(700, 500, "TestWindow")
    # window.create_child(300, 200)
    window.run()