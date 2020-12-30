import tkinter as tk
import tkutils
import constants
import socket


class StartView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=constants.WINDOW_WIDTH_PX, height=constants.WINDOW_HEIGHT_PX,
                          bg=constants.COLOR_MIDNIGHT_BLUE)
        self.controller = controller

        title = tk.Label(self, text="BattleShips", font=controller.title_font, fg=constants.COLOR_CLOUDS, bg=constants.COLOR_MIDNIGHT_BLUE)
        title.pack(side="top", pady=20)

        row1 = tk.Frame(self, bg=constants.COLOR_MIDNIGHT_BLUE)
        row1.pack(side="top", pady=60)

        create_game_label = tk.Label(row1, text="Create a game:", font=controller.base_font, fg=constants.COLOR_CLOUDS, bg=constants.COLOR_MIDNIGHT_BLUE)
        create_game_label.pack(side="left", padx=30)

        ip_port_frame = tk.Frame(row1, bg=constants.COLOR_MIDNIGHT_BLUE)
        ip_port_frame.pack(side="left", padx=30)

        ip_frame = tk.Frame(ip_port_frame, bg=constants.COLOR_MIDNIGHT_BLUE)
        ip_frame.pack(side="top", pady=3)

        ip_label1 = tk.Label(ip_frame, text="IP:", font=controller.secondary_font, fg=constants.COLOR_CLOUDS, bg=constants.COLOR_MIDNIGHT_BLUE)
        ip_label1.pack(side="left")
        ip_label2 = tk.Label(ip_frame, text=socket.gethostbyname(socket.gethostname()), font=controller.monospace_font, fg=constants.COLOR_CLOUDS, bg=constants.COLOR_MIDNIGHT_BLUE)
        ip_label2.pack(side="left")

        port_frame = tk.Frame(ip_port_frame, bg=constants.COLOR_MIDNIGHT_BLUE)
        port_frame.pack(side="top", pady=3)

        port_label = tk.Label(port_frame, text="port: ", font=controller.secondary_font, fg=constants.COLOR_CLOUDS, bg=constants.COLOR_MIDNIGHT_BLUE)
        port_label.pack(side="left")

        port_string = tk.StringVar()
        port_string.set(28778)
        port_string.trace("w", lambda *args: tkutils.character_limit(port_string, 5))

        port_entry = tk.Entry(port_frame, textvariable=port_string, font=controller.monospace_font, width=5)
        port_entry.pack(side="left")

        button = tk.Button(row1, text="Create", font=controller.secondary_font, command=lambda: controller.show_frame("GameView"), width=10)
        button.pack(side="left", padx=30)

        row2 = tk.Frame(self, bg=constants.COLOR_MIDNIGHT_BLUE)
        row2.pack(side="top", pady=20)

        join_game_label = tk.Label(row2, text="Join a game:", font=controller.base_font, fg=constants.COLOR_CLOUDS, bg=constants.COLOR_MIDNIGHT_BLUE)
        join_game_label.pack(side="left", padx=30)

        ip_port_frame2 = tk.Frame(row2, bg=constants.COLOR_MIDNIGHT_BLUE)
        ip_port_frame2.pack(side="left", padx=30)

        ip_frame2 = tk.Frame(ip_port_frame2, bg=constants.COLOR_MIDNIGHT_BLUE)
        ip_frame2.pack(side="top", pady=3)

        ip_label = tk.Label(ip_frame2, text="IP: ", font=controller.secondary_font, fg=constants.COLOR_CLOUDS, bg=constants.COLOR_MIDNIGHT_BLUE)
        ip_label.pack(side="left")

        ip_string = tk.StringVar()
        ip_string.set("111.111.111.111")
        ip_string.trace("w", lambda *args: tkutils.character_limit(ip_string, 15))

        ip_entry = tk.Entry(ip_frame2, textvariable=ip_string, font=controller.monospace_font, width=15)
        ip_entry.pack(side="left")

        port_frame2 = tk.Frame(ip_port_frame2, bg=constants.COLOR_MIDNIGHT_BLUE)
        port_frame2.pack(side="top", pady=3)

        port_label2 = tk.Label(port_frame2, text="port: ", font=controller.secondary_font, fg=constants.COLOR_CLOUDS, bg=constants.COLOR_MIDNIGHT_BLUE)
        port_label2.pack(side="left")

        port_string2 = tk.StringVar()
        port_string2.set(28778)
        port_string2.trace("w", lambda *args: tkutils.character_limit(port_string, 5))

        port_entry2 = tk.Entry(port_frame2, textvariable=port_string2, font=controller.monospace_font, width=5)
        port_entry2.pack(side="left")

        button = tk.Button(row2, text="Join", font=controller.secondary_font, command=lambda: controller.show_frame("GameView"), width=10)
        button.pack(side="left", padx=30)
