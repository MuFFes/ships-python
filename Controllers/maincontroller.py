import tkinter as tk
import tkinter.font

import constants
import Views.endview
import Views.gameview
import Views.startview


class MainController(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry(constants.WINDOW_SIZE)
        self.resizable(False, False)

        self.__fonts = {
            "main": tk.font.Font(**constants.FONT_MAIN),
            "title": tk.font.Font(**constants.FONT_TITLE),
            "secondary": tk.font.Font(**constants.FONT_SECONDARY),
            "monospace": tk.font.Font(**constants.FONT_MONOSPACE)
        }
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_configure(column=0, row=0)

        self.views = [
            Views.startview.StartView,
            Views.gameview.GameView,
            Views.endview.EndView
        ]
        self.frames = {}

        for F in self.views:
            self.frames[F.__name__] = F(parent=container, controller=self)
            self.frames[F.__name__].grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartView")

    def show_frame(self, page_name):
        self.frames[page_name].tkraise()

    def get_font(self, font_type):
        return self.__fonts.get(font_type)

    def create_server(self):
        pass