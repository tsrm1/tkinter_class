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
        # self.label1.pack(anchor=NW)

        Label(self.root, width=30, height=2, bg='red', text="First").pack()
        Label(self.root, width=30, height=2, bg='orange', text="Second").pack()
        Label(self.root, width=30, height=2, bg='yellow', text="Third").pack()
        Label(self.root, width=30, height=2, bg='green', text="Fourth").pack()

        # # pack(side=TOP) - по умолчанию side=TOP, /BOTTOM, LEFT, RIGHT,
        # Label(self.root, width=30, height=2, bg='red', text="First").pack(side=BOTTOM)
        # Label(self.root, width=30, height=2, bg='orange', text="Second").pack(side=BOTTOM)
        # Label(self.root, width=30, height=2, bg='yellow', text="Third").pack(side=BOTTOM)
        # Label(self.root, width=30, height=2, bg='green', text="Fourth").pack(side=BOTTOM)

    def draw_widgets_in_frames(self):
        top_frame = Frame(self.root)
        bottom_frame = Frame(self.root)

        top_label_frame = LabelFrame(self.root, text="Top frame")
        bottom_label_frame = LabelFrame(self.root, text="Bottom frame")

        top_frame.pack()
        bottom_frame.pack()
        top_label_frame.pack(padx=10, pady=10, expand=1)
        bottom_label_frame.pack(ipadx=10, ipady=10, expand=1)

        # padx, pady - внешние отступы выджета
        # ipadx, ipady - внутркнние отступы выджета
        # expand=1 - при расширении окна, выравнивание по центру
        # fill=X - растянуть виджет по оси X
        # fill=Y - растянуть виджет по оси Y
        # fill=BOTH - растянуть виджет по обеим осям
        # anchor=NW - расположение виджета в левом верхнем углу (NW, N, NE, E, SE, S, SW, W, NWNS)
        # side=BOTTOM расположение виджета в внизу по оси (TOP, BOTTOM, LEFT, RIGHT, CENTER)


        Label(top_frame, width=30, height=2, bg='red', text="First").pack(side=LEFT)
        Label(top_frame, width=30, height=2, bg='orange', text="Second").pack(side=LEFT)
        Label(bottom_frame, width=30, height=2, bg='yellow', text="Third").pack(side=LEFT)
        Label(bottom_frame, width=30, height=2, bg='green', text="Fourth").pack(side=LEFT)

        Label(top_label_frame, width=30, height=2, bg='red', text="First").pack(side=LEFT)
        Label(top_label_frame, width=30, height=2, bg='orange', text="Second").pack(side=LEFT)
        Label(bottom_label_frame, width=30, height=2, bg='yellow', text="Third").pack(side=LEFT)
        Label(bottom_label_frame, width=30, height=2, bg='green', text="Fourth").pack(side=LEFT)
        Label(bottom_label_frame, width=30, height=2, bg='cyan', text="Fifth").pack(side=LEFT, padx=10)


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