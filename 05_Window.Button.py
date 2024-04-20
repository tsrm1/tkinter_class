# https://www.youtube.com/watch?v=tpU-vYq3H-4

from tkinter import *
from PIL import Image as PilImage
from PIL import ImageTk


class Window:
    def __init__(self, width, height, title="MyWindow", resizable=(True, True), icon="ico/favicon.ico") -> None:
        self.root = Tk()                                # Инициалиция окна
        self.root.title(title)                          # название окна
        self.root.geometry(f"{width}x{height}+100+100") # "Ширина x Высота + Смещение по X + Смещение по Y"
        # self.root.minsize(400,300)                      # минимальные размеры: ширина - 200, высота - 150
        self.root.resizable(resizable[0], resizable[1]) # изменение окна по осям              
        if icon !="":
            self.root.iconbitmap(icon)                  # установка иконки для окна
        
        img = PilImage.open('./ico/icon2.png')
        img = img.resize((28, 28), PilImage.LANCZOS)
        self.photo_image = ImageTk.PhotoImage(img)

        self.label = Label(self.root, width=45, height=2, text="Change color", bg='cyan')


    def button_action(self):
        print('Print Button clicked!')

    def create_label(self):
        Label(self.root, text="New Label").pack(anchor=NW)

    def change_label(self):
        self.root.label.configure(text="Pressed", bg="red")

    def change_color(self, color):
        self.label.configure(text=color, fg=color)
        self.root.configure(bg=color)

        
    def draw_widgets(self):
        Button(self.root, text="Destroy", width=20, command=self.root.destroy).pack(anchor=NW)  # закрытие окна графического интерфейса
        Button(self.root, text="Quit", width=20, command=quit).pack(anchor=NW)                  # закрытие программы

        Button(self.root, width=30, height=5, text="Press Button", relief=GROOVE, bd=8).pack(side=LEFT, anchor=NW)
        Button(self.root, width=30, height=5, text="New Button", font=("Consolas", 10, "bold"), wraplength=15, justify=LEFT, underline=0).pack(side="top", anchor=NW)
        Button(self.root, image=self.photo_image).pack(side=LEFT, anchor=NW)
        Button(self.root, text='image', image=self.photo_image, compound=LEFT).pack(side=LEFT, anchor=NW)
        Button(self.root, text='OK', bg="green", fg='yellow', activebackground='yellow', activeforeground='green').pack(side=LEFT, anchor=NW)
        Button(self.root, text='Print', command=self.button_action).pack(side=LEFT, anchor=NW)
        
        self.label.pack(side=TOP, anchor=NW)
        Button(self.root, text='red', bg='red', width=10, command=lambda: self.change_color("red")).pack(side=LEFT, anchor=NW)
        Button(self.root, text='orange', bg='orange', width=10, command=lambda: self.change_color("orange")).pack(side=LEFT, anchor=NW)
        Button(self.root, text='yellow', bg='yellow', width=10, command=lambda: self.change_color("yellow")).pack(side=LEFT, anchor=NW)
        Button(self.root, text='green', bg='green', width=10, command=lambda: self.change_color("green")).pack(side=LEFT, anchor=NW)

        Button(self.root, text='Create Label', command=self.create_label).pack(side=TOP, anchor=NW)


    def run(self):
        self.draw_widgets()             # прорисовка виджетов в окне root
        # self.draw_widgets_in_frames()   # прорисовка виджетов в рамках, которые находяться в окне root
        self.root.mainloop()


if __name__ == "__main__":
    window = Window(950, 500, "TestWindow")
    window.run()