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
        
        self.login_entry = Entry(self.root)
        self.email_entry = Entry(self.root)
        self.age_entry = Entry(self.root)
        self.password_entry = Entry(self.root, show="*")    # маскируем текст при вводе


    def draw_widgets(self):
        Label(self.root, text="Login:", justify=LEFT).grid(row=0, column=0, sticky=W)
        self.login_entry.grid(row=0, column=1, sticky=W+E, padx=5, pady=5)

        Label(self.root, text="E-Mail:", justify=LEFT).grid(row=1, column=0, sticky=W)
        self.email_entry.grid(row=1, column=1, sticky=W+E, padx=5, pady=5)

        Label(self.root, text="Age:", justify=LEFT).grid(row=2, column=0, sticky=W)
        self.age_entry.grid(row=2, column=1, sticky=W+E, padx=5, pady=5)

        Label(self.root, text="Password:", justify=LEFT).grid(row=3, column=0, sticky=W)
        self.password_entry.grid(row=3, column=1, sticky=W+E, padx=5, pady=5)

        Button(self.root, text="Save", width=10, command=self.save_data).grid(row=4, column=0, padx=5, sticky=W)
        Button(self.root, text="Quit", width=10, command=self.exit).grid(row=4, column=1, sticky=E)

    def exit(self):
        choice = messagebox.askyesno("Quit", "Do you want to quit?")            # Да/Нет = True/False
        # choice = messagebox.askokcancel("Quit", "Do you want to quit?")       # ОК/Отмена = True/False
        # choice = messagebox.askretrycancel("Quit", "Do you want to quit?")    # Повтор/Отмена = True/False
        # choice = messagebox.askyesnocancel("Quit", "Do you want to quit?")    # Да/Нет/Отмена = True/False/None
        
        print(f'Quit={choice}')
        if choice:
            self.root.destroy()

    def save_data(self):
        login = self.login_entry.get()
        email = self.email_entry.get()
        age = int(self.age_entry.get())         # переводим в число
        password = self.password_entry.get()

        messagebox.showinfo("User Data", f"Hello, {login}! You're {age} years old. E-Mail: {email}")

    def run(self):
        self.draw_widgets()             # прорисовка виджетов в окне root
        self.root.mainloop()


if __name__ == "__main__":
    window = Window(300, 300, "TestWindow", resizable=(False, False))
    window.run()