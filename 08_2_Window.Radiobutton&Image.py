# https://www.youtube.com/watch?v=2Ye9UzuthZc

from tkinter import *
from tkinter import messagebox
from PIL import Image as PilImage
from PIL import ImageTk, ImageOps

class Window:
    def __init__(self, width, height, title="MyWindow", resizable=(True, True), icon="ico/favicon.ico") -> None:
        self.root = Tk()                                # Инициалиция окна
        self.root.title(title)                          # название окна
        self.root.geometry(f"{width}x{height}+100+100") # "Ширина x Высота + Смещение по X + Смещение по Y"
        # self.root.minsize(400,300)                      # минимальные размеры: ширина - 200, высота - 150
        self.root.resizable(resizable[0], resizable[1]) # изменение окна по осям              
        if icon !="":
            self.root.iconbitmap(icon)                  # установка иконки для окна
        
        self.choice = StringVar(value='telegram')

        img1 = PilImage.open("./ico/viber.png")
        neg1 = ImageOps.invert(img1.convert("RGB"))
        img1 = img1.resize((20,20), PilImage.LANCZOS)
        neg1 = neg1.resize((20, 20), PilImage.LANCZOS)
        self.smile1 = ImageTk.PhotoImage(img1)
        self.neg_smile1 = ImageTk.PhotoImage(neg1)

        img2 = PilImage.open("./ico/telegram.png")
        neg2 = ImageOps.invert(img2.convert("RGB"))
        img2 = img2.resize((20,20), PilImage.LANCZOS)
        neg2 = neg2.resize((20, 20), PilImage.LANCZOS)
        self.smile2 = ImageTk.PhotoImage(img2)
        self.neg_smile2 = ImageTk.PhotoImage(neg2)

        img3 = PilImage.open("./ico/whatsup.png")
        neg3 = ImageOps.invert(img3.convert("RGB"))
        img3 = img3.resize((20,20), PilImage.LANCZOS)
        neg3 = neg3.resize((20, 20), PilImage.LANCZOS)
        self.smile3 = ImageTk.PhotoImage(img3)
        self.neg_smile3 = ImageTk.PhotoImage(neg3)



    def draw_widgets(self):
        
        Radiobutton(self.root, text='Viber', variable=self.choice, value='viber' ,relief=SUNKEN, bd=2, image=self.smile1, selectimage=self.neg_smile1).pack(anchor=NW, padx=10)
        Radiobutton(self.root, text='Telegram', variable=self.choice, value='telegram' ,relief=SUNKEN, bd=2, image=self.smile2, selectimage=self.neg_smile2).pack(anchor=NW, padx=10)
        Radiobutton(self.root, text='Whatsup', variable=self.choice, value='whatsup' ,relief=SUNKEN, bd=2, image=self.smile3, selectimage=self.neg_smile3).pack(anchor=NW, padx=10)
        
        
        Button(self.root, text="Save", width=10, command=self.choice_info).pack(anchor=NW, padx=10)
        Button(self.root, text="Quit", width=10, command=self.exit).pack(anchor=NW, padx=10)

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