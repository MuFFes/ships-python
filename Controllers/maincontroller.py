import tkinter as tk

import clientconnection
import constants
import game
import Views.endview
import Views.gameview
import Views.startview
import serverconnection


class MainController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(constants.WINDOW_SIZE)
        self.root.resizable(False, False)

        self.game = None
        self.views = [
            Views.startview.StartView,
            Views.gameview.GameView,
            Views.endview.EndView
        ]
        self.frames = {}

        container = tk.Frame(self.root)
        container.pack(side="top", fill="both", expand=True)
        container.grid_configure(column=0, row=0)

        for F in self.views:
            self.frames[F.__name__] = F(parent=container, controller=self)
            self.frames[F.__name__].grid(row=0, column=0, sticky="nsew")

        self.show_frame("GameView")
        self.root.mainloop()

    def show_frame(self, page_name):
        self.frames[page_name].tkraise()

    def create_game(self, port_string):
        connection = serverconnection.ServerConnection(int(port_string))
        g = game.Game(connection=connection, is_server=True)
        g.start()
        self.show_frame("GameView")

    def join_game(self, ip_string, port_string):
        connection = clientconnection.ClientConnection(ip_string, int(port_string))
        g = game.Game(connection=connection, is_server=False)
        g.start()
        self.show_frame("GameView")

