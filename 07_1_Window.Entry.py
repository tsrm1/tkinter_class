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
        
        self.entry = Entry(self.root, width=30, fg='yellow', bg='black', font=("Verdana", 9, "bold"), justify=RIGHT, relief=SUNKEN, bd=3, selectbackground='yellow', selectforeground='red')

        # self.entry.selection_from(0) # выделение текста с индекса 0
        # self.entry.selection_adjust(0) # 
        # self.entry.selection_to(0) # от ANCHOR до ...
        # self.entry.selection_range(1, 2) # от pos1 до pos2
        # self.entry.selection_present() # есть выделение или нет, TRUE/FALSE
        # self.entry.selection_clear() # снятие выделения

        




    def draw_widgets(self):
        # Entry(self.root, width=30, fg='yellow', bg='black', font=("Verdana", 9, "bold"), justify=RIGHT, relief=SUNKEN, bd=3, selectbackground='yellow', selectforeground='red').pack()
        self.entry.pack()
        Button(self.root, text="Show text", width=10, command=self.get_text).pack()
        Button(self.root, text="Repeat text", width=10, command=self.repeat_text).pack()
        Button(self.root, text="Insert text", width=10, command=self.insert).pack()
        Button(self.root, text="Clear text", width=10, command=self.clear).pack()

        Button(self.root, text="Quit", width=10, command=self.exit).pack()

    def exit(self):
        choice = messagebox.askyesno("Quit", "Do you want to quit?")            # Да/Нет = True/False
        # choice = messagebox.askokcancel("Quit", "Do you want to quit?")       # ОК/Отмена = True/False
        # choice = messagebox.askretrycancel("Quit", "Do you want to quit?")    # Повтор/Отмена = True/False
        # choice = messagebox.askyesnocancel("Quit", "Do you want to quit?")    # Да/Нет/Отмена = True/False/None

        print(choice)
        if choice:
            self.root.destroy()

    def get_text(self):
        text = self.entry.get()
        messagebox.showinfo("Entry text", text)

    def repeat_text(self):
        text = self.entry.get()
        self.entry.insert(0, text)      # вставляем текст вначале
        self.entry.insert(END, text)    # вставляем текст вконце

    def insert(self):
        self.entry.insert(INSERT, '_insert_')   # вставить '..' до курсора/выделения
        self.entry.insert(ANCHOR, '_selected_') # вставить '..' после курсора/выделения

    def clear(self):
        self.entry.delete(0, END)
    
    def run(self):
        self.draw_widgets()             # прорисовка виджетов в окне root
        self.root.mainloop()


if __name__ == "__main__":
    window = Window(300, 300, "TestWindow", resizable=(False, False))
    window.run()