import tkinter as tk
import threading
import queue

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
        self.root.title("BattleShips")

        self.game = None
        self.views = [
            startview.StartView,
            gameview.GameView,
        ]
        self.frames = {}
        self.__mouse_position = (-1, -1)
        self.__placed = False
        # For multithreading
        self.queue = queue.Queue()

        self.__setup_views()
        self.__show_frame("StartView")
        self.__update_gameview()

    def __update_gameview(self):
        if self.game:
            if self.game.update_pending:
                self.frames["GameView"].update_view(self.game)
                self.game.update_pending = False
        self.root.after(50, self.__update_gameview)

    def __setup_views(self):
        container = tk.Frame(self.root)
        container.pack(side="top", fill="both", expand=True)
        container.grid_configure(column=0, row=0)

        for F in self.views:
            self.frames[F.__name__] = F(parent=container, controller=self)
            self.frames[F.__name__].grid(row=0, column=0, sticky="nsew")

    def __show_frame(self, page_name):
        self.frames[page_name].tkraise()

    def process_queue(self, callback=None):
        try:
            msg = self.queue.get(block=False)
            if callback:
                callback()
        except queue.Empty:
            self.root.after(100, lambda: self.process_queue(callback))

    def start_threaded_task(self, task, args, callback=None):
        thread = threading.Thread(target=task, args=(self.queue, *args), daemon=True)
        thread.start()
        self.process_queue(callback)

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
        if self.game.phase == game.GamePhase.SETUP_SHIPS:
            if self.game.place_ship(event.x // constants.TILE_SIZE_PX, event.y // constants.TILE_SIZE_PX):
                self.frames["GameView"].update_view(self.game)
                self.root.configure(cursor="arrow")
                self.__placed = True

                if self.game.phase == game.GamePhase.SETUP_WAIT:
                    self.start_threaded_task(task=self.game.finish_setup, args=())
        else:
            self.frames["GameView"].my_field_canvas.unbind("<Button-1>")

    def my_field_canvas_mouse_motion(self, event):
        if self.game.phase == game.GamePhase.SETUP_SHIPS:
            (x, y) = (event.x // constants.TILE_SIZE_PX, event.y // constants.TILE_SIZE_PX)
            if self.__mouse_position != (x, y):
                self.root.configure(cursor="arrow")
                if self.game.validate_ship_position(x, y):
                    self.root.configure(cursor="hand2")
                    if not self.__placed:
                        self.frames["GameView"].clear_ghost_ship(self.__mouse_position[0], self.__mouse_position[1],
                                                                 self.game.ships_size[0], self.game.ship_orientation)
                    self.__placed = False
                    self.__mouse_position = (x, y)
                    self.frames["GameView"].show_ghost_ship(x, y, self.game.ships_size[0], self.game.ship_orientation)
        else:
            self.frames["GameView"].my_field_canvas.unbind("<Motion>")

    def enemy_field_canvas_click(self, event):
        if self.game.phase == game.GamePhase.SHOOT:
            (x, y) = (event.x // constants.TILE_SIZE_PX, event.y // constants.TILE_SIZE_PX)
            self.start_threaded_task(task=self.game.shoot, args=(x, y))

    def enemy_field_canvas_mouse_motion(self, event):
        if self.game.phase == game.GamePhase.SHOOT:
            self.root.configure(cursor="hand2")
        else:
            self.root.configure(cursor="arrow")

    def key_press(self, event):
        if self.game.phase == game.GamePhase.SETUP_SHIPS:
            self.game.ship_orientation = (self.game.ship_orientation + 1) % 2
            self.frames["GameView"].update_view(self.game)
            if self.game.validate_ship_position(self.__mouse_position[0], self.__mouse_position[1]):
                self.frames["GameView"].show_ghost_ship(self.__mouse_position[0], self.__mouse_position[1], self.game.ships_size[0], self.game.ship_orientation)
        else:
            self.frames["GameView"].canvas.unbind("<Key>")


if __name__ == '__main__':
    assets.Assets.load()
    application = MainApplication()
    application.root.mainloop()
