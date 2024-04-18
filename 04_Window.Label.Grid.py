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
        Label(self.root, width=30, height=2, bg='red', text="First").grid(row=0, column=0)
        Label(self.root, width=30, height=2, bg='orange', text="Second").grid(row=0, column=1)
        Label(self.root, width=30, height=2, bg='yellow', text="Third").grid(row=0, column=2)
        Label(self.root, width=30, height=2, bg='green', text="Fourth").grid(row=0, column=3)

        Label(self.root, width=5, height=2, bg='yellow', text="Fiveth").grid(row=0, rowspan=6, column=4, sticky=N+S)

        Label(self.root, width=30, height=2, bg='orange', text="First").grid(row=1, column=0)
        Label(self.root, width=30, height=2, bg='yellow', text="Second").grid(row=1, column=1)
        Label(self.root, width=30, height=2, bg='red', text="Third").grid(row=1,  column=2, columnspan=2, sticky=E+W)
        
        big_label = Label(self.root, width=30, height=10, bg='cyan', text="Fourth")
        small_label = Label(self.root, width=30, height=2, bg='red', text="Third")

        big_label.grid(row=2, rowspan=3, column=0, columnspan=4, sticky=N+E+S+W)
        small_label.grid(row=3, column=1, columnspan=2, sticky=N+E+S+W)

        Label(self.root, width=30, height=2, bg='red', text="First").grid(row=5, column=0)
        Label(self.root, width=30, height=2, bg='orange', text="Second").grid(row=5, column=1)
        Label(self.root, width=30, height=2, bg='yellow', text="Third").grid(row=5, column=2)
        Label(self.root, width=30, height=2, bg='green', text="Fourth").grid(row=5, column=3)
       
        Label(self.root, width=30, height=2, bg='cyan', text="First").grid(row=6, column=0, columnspan=4, sticky=E+W)



        small_label.grid_remove()   # скрытие виджета с экрана 
        small_label.grid()          # прорисовка ранее скрытого виджета 
        # small_label.forget()        # удаление месторасположения ранее выведеного виджета 
        
        print(big_label.grid_info())    # получим словарь с месторасположением виджета
        print(self.root.grid_size())    # получим словарь с размером слновной таблицы
        print(self.root.grid_location(x=50, y=50))  # возвращает ячейку, к которой максимально приближены координаты

    def run(self):
        self.draw_widgets()             # прорисовка виджетов в окне root
        # self.draw_widgets_in_frames()   # прорисовка виджетов в рамках, которые находяться в окне root
        self.root.mainloop()

    
    def create_child(self, width, height, title="ChildWindow", resizable=(True, True), icon="ico/favicon.ico") -> None:
        ChildWindow(self.root, width, height, title, resizable, icon)


if __name__ == "__main__":
    window = Window(950, 500, "TestWindow")
    # window.create_child(300, 200)
    window.run()