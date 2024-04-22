# https://www.youtube.com/watch?v=2Ye9UzuthZc

from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox


class Window:
    def __init__(self, width, height, title="MyWindow", resizable=(False, False), icon="ico/favicon.ico") -> None:
        self.root = Tk()                                # Инициалиция окна
        self.root.title(title)                          # название окна
        self.root.geometry(f"{width}x{height}+100+100") # "Ширина x Высота + Смещение по X + Смещение по Y"
        # self.root.geometry(f"+100+100") # "Ширина x Высота + Смещение по X + Смещение по Y"
        # self.root.minsize(400,300)                      # минимальные размеры: ширина - 200, высота - 150
        self.root.resizable(resizable[0], resizable[1]) # изменение окна по осям              
        if icon !="":
            self.root.iconbitmap(icon)                  # установка иконки для окна
        
        self.auto_load = BooleanVar(value=0)
        self.auto_save = BooleanVar(value=0)
        self.fullscreen = BooleanVar(value=1)
        self.screen_size = StringVar(value='1920x1080')

    def draw_menu(self):
        menu_bar = Menu(self.root)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='Open file', command=self.cmd_open_file)
        file_menu.add_command(label='Open folder', command=self.cmd_open_folder)
        file_menu.add_separator()
        file_menu.add_command(label='Save', command=self.cmd_save)
        file_menu.add_command(label='Save as...', command=self.cmd_save_as)
        file_menu.add_separator()
        file_menu.add_checkbutton(label="Autoload", offvalue=0, onvalue=1, variable=self.auto_load, command=self.cmd_check_auto_load)
        file_menu.add_checkbutton(label="Autosave", offvalue=0, onvalue=1, variable=self.auto_save, command=self.cmd_auto_save_changed)
        file_menu.add_separator()
        file_menu.add_command(label='Quit', command=self.cmd_exit)

        screen_size_menu = Menu(menu_bar, tearoff=0)
        screen_size_menu.add_radiobutton(label="800x600", value="800x600", variable=self.screen_size, command=self.cmd_screen_size_changed)
        screen_size_menu.add_radiobutton(label="1280x720", value="1280x720", variable=self.screen_size, command=self.cmd_screen_size_changed)
        screen_size_menu.add_radiobutton(label="1600x1400", value="1600x1400", variable=self.screen_size, command=self.cmd_screen_size_changed)
        screen_size_menu.add_radiobutton(label="1920x1080", value="1920x1080", variable=self.screen_size, command=self.cmd_screen_size_changed)

        view_menu = Menu(menu_bar, tearoff=0)
        view_menu.add_checkbutton(label="Fulscreen", offvalue=0, onvalue=1, variable=self.fullscreen)
        view_menu.add_separator()
        view_menu.add_cascade(label="Screensize", menu=screen_size_menu)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.cmd_about)

        menu_bar.add_cascade(label="File", menu=file_menu)
        # menu_bar.add_command(label='Edit', command=self.cmd_edit)
        menu_bar.add_cascade(label='View', menu=view_menu)
        menu_bar.add_cascade(label='Help', menu=help_menu)

        self.root.configure(menu=menu_bar)
    
    def cmd_open_file(self):
        pass

    def cmd_open_folder(self):
        pass

    def cmd_save(self):
        pass

    def cmd_save_as(self):
        pass

    def cmd_auto_save_changed(self):
        messagebox.showinfo("Autosave", f"Value: {self.auto_save.get()}")

    def cmd_check_auto_load(self):
        if not self.auto_save.get() and self.auto_load.get():
            if messagebox.askyesno("Error", "Autoload without autosave.\nDo you want set autosave?"):
                self.auto_save.set(True)


    def cmd_screen_size_changed(self):
        messagebox.showinfo("Screensize", f"Value: {self.screen_size.get()}")

    def cmd_view(self):
        pass

    def cmd_about(self):
        messagebox.showinfo("Banderogusak", "Banderogusak is a best game in the world!\nVersion: 2.0")
    
    def draw_widgets(self):
        self.draw_menu()
        Label(self.root, text="Just a label").pack(anchor=NW)

        # Button(self.root, text="Quit", width=10, command=self.exit).pack(anchor=NW, padx=10)
    

    def cmd_exit(self):
        choice = messagebox.askyesno("Quit", "Do you want to quit?")            # Да/Нет = True/False
        # choice = messagebox.askokcancel("Quit", "Do you want to quit?")       # ОК/Отмена = True/False
        # choice = messagebox.askretrycancel("Quit", "Do you want to quit?")    # Повтор/Отмена = True/False
        # choice = messagebox.askyesnocancel("Quit", "Do you want to quit?")    # Да/Нет/Отмена = True/False/None
        
        print(f'Quit={choice}')
        if choice:
            self.root.destroy()

    def run(self):
        self.draw_widgets()             # прорисовка виджетов в окне root
        self.root.mainloop()


if __name__ == "__main__":
    window = Window("300", "300", "TestWindow", resizable=(False, False))
    window.run()