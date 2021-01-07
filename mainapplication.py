import tkinter as tk

import assets
import constants
import game
from Views import gameview, startview
from Connection import clientconnection, serverconnection


class MainApplication:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(constants.WINDOW_SIZE)
        self.root.resizable(False, False)

        self.game = None
        self.views = [
            startview.StartView,
            gameview.GameView,
        ]
        self.frames = {}

        self.__setup_views()
        self.__show_frame("StartView")

    def __setup_views(self):
        container = tk.Frame(self.root)
        container.pack(side="top", fill="both", expand=True)
        container.grid_configure(column=0, row=0)

        for F in self.views:
            self.frames[F.__name__] = F(parent=container, controller=self)
            self.frames[F.__name__].grid(row=0, column=0, sticky="nsew")

    def __show_frame(self, page_name):
        self.frames[page_name].tkraise()

    def create_game_button_click(self, port_string):
        connection = serverconnection.ServerConnection(int(port_string))
        self.game = game.Game(connection=connection, is_server=True)
        self.__show_frame("GameView")
        self.game.start()
        self.frames["GameView"].update_view(self.game)

    def join_game_button_click(self, ip_string, port_string):
        connection = clientconnection.ClientConnection(ip_string, int(port_string))
        self.game = game.Game(connection=connection, is_server=False)
        self.__show_frame("GameView")
        self.game.start()
        self.frames["GameView"].update_view(self.game)

    def my_field_canvas_click(self, event):
        pass

    def my_field_canvas_mouse_move(self, event):
        pass

    def enemy_field_canvas_click(self, event):
        self.game.shoot(event.x // constants.TILE_SIZE_PX,
                        event.y // constants.TILE_SIZE_PX)
        self.frames["GameView"].update_view(self.game)

    def enemy_field_canvas_mouse_move(self, event):
        pass


if __name__ == '__main__':
    assets.Assets.load()
    application = MainApplication()
    application.root.mainloop()
