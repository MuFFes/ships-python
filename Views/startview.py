import tkinter as tk
import tkutils
import constants as c
import socket


class StartView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=c.WINDOW_WIDTH_PX, height=c.WINDOW_HEIGHT_PX,
                          bg=c.COLOR_MIDNIGHT_BLUE)

        title_font = tkutils.get_font("title")
        main_font = tkutils.get_font("main")
        secondary_font = tkutils.get_font("secondary")
        monospace_font = tkutils.get_font("monospace")

        # Game title
        tk.Label(self, text="BattleShips", font=title_font, fg=c.COLOR_CLOUDS, bg=c.COLOR_MIDNIGHT_BLUE).pack(side="top", pady=20)

        # First row container
        row1 = tk.Frame(self, bg=c.COLOR_MIDNIGHT_BLUE)
        row1.pack(side="top", pady=60)

        # Create game label
        tk.Label(row1, text="Create a game:", font=main_font, fg=c.COLOR_CLOUDS, bg=c.COLOR_MIDNIGHT_BLUE).pack(side="left", padx=30)

        # Container for IP and Port containers
        ip_port_frame = tk.Frame(row1, bg=c.COLOR_MIDNIGHT_BLUE)
        ip_port_frame.pack(side="left", padx=30)

        # Container for IP
        ip_frame = tk.Frame(ip_port_frame, bg=c.COLOR_MIDNIGHT_BLUE)
        ip_frame.pack(side="top", pady=3)

        tk.Label(ip_frame, text="IP:", font=secondary_font, fg=c.COLOR_CLOUDS, bg=c.COLOR_MIDNIGHT_BLUE).pack(side="left")
        tk.Label(ip_frame, text=socket.gethostbyname(socket.gethostname()), font=monospace_font, fg=c.COLOR_CLOUDS, bg=c.COLOR_MIDNIGHT_BLUE).pack(side="left")

        # Container for Port
        port_frame = tk.Frame(ip_port_frame, bg=c.COLOR_MIDNIGHT_BLUE)
        port_frame.pack(side="top", pady=3)

        tk.Label(port_frame, text="port: ", font=secondary_font, fg=c.COLOR_CLOUDS, bg=c.COLOR_MIDNIGHT_BLUE).pack(side="left")
        port_string = tk.StringVar(value="28778")
        port_string.trace("w", lambda *args: tkutils.character_limit(port_string, 5))
        tk.Entry(port_frame, textvariable=port_string, font=monospace_font, width=5).pack(side="left")

        # Create game button
        tk.Button(row1, text="Create", font=secondary_font, command=lambda: controller.create_game_button_click(port_string.get()), width=10).pack(side="left", padx=30)

        # Second row container
        row2 = tk.Frame(self, bg=c.COLOR_MIDNIGHT_BLUE)
        row2.pack(side="top", pady=20)

        # Join game label
        tk.Label(row2, text="Join a game:", font=main_font, fg=c.COLOR_CLOUDS, bg=c.COLOR_MIDNIGHT_BLUE).pack(side="left", padx=30)

        # Container for IP and Port
        ip_port_frame = tk.Frame(row2, bg=c.COLOR_MIDNIGHT_BLUE)
        ip_port_frame.pack(side="left", padx=30)

        ip_frame2 = tk.Frame(ip_port_frame, bg=c.COLOR_MIDNIGHT_BLUE)
        ip_frame2.pack(side="top", pady=3)

        # IP label and entry
        tk.Label(ip_frame2, text="IP: ", font=secondary_font, fg=c.COLOR_CLOUDS, bg=c.COLOR_MIDNIGHT_BLUE).pack(side="left")
        ip_string = tk.StringVar(value="localhost")
        ip_string.trace("w", lambda *args: tkutils.character_limit(ip_string, 15))
        tk.Entry(ip_frame2, textvariable=ip_string, font=monospace_font, width=15).pack(side="left")

        # Container for port
        port_frame2 = tk.Frame(ip_port_frame, bg=c.COLOR_MIDNIGHT_BLUE)
        port_frame2.pack(side="top", pady=3)

        # Port label and entry
        tk.Label(port_frame2, text="port: ", font=secondary_font, fg=c.COLOR_CLOUDS, bg=c.COLOR_MIDNIGHT_BLUE).pack(side="left")
        port_string2 = tk.StringVar(value="28778")
        port_string2.trace("w", lambda *args: tkutils.character_limit(port_string, 5))
        tk.Entry(port_frame2, textvariable=port_string2, font=monospace_font, width=5).pack(side="left")

        # Join game button
        tk.Button(row2, text="Join", font=secondary_font, command=lambda: controller.join_game_button_click(ip_string.get(), port_string2.get()), width=10).pack(side="left", padx=30)
