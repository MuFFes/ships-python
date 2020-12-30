import tkinter as tk
import tkinter.font

import constants
import endview
import gameview
import startview


class MainController(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry(constants.WINDOW_SIZE)
        self.resizable(False, False)
        self.base_font = tk.font.Font(**constants.FONT_BASE)
        self.title_font = tk.font.Font(**constants.FONT_TITLE)
        self.secondary_font = tk.font.Font(**constants.FONT_SECONDARY)
        self.monospace_font = tk.font.Font(**constants.FONT_MONOSPACE)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_configure(column=0, row=0)

        self.frames = {}
        self.views = [
            startview.StartView,
            gameview.GameView,
            endview.EndView
        ]
        for F in self.views:
            self.frames[F.__name__] = F(parent=container, controller=self)
            self.frames[F.__name__].grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartView")

    def show_frame(self, page_name):
        self.frames[page_name].tkraise()
