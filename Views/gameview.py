import tkinter as tk

import constants as c
import tkutils
from game import Orientation


class GameView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, width=c.WINDOW_WIDTH_PX, height=c.WINDOW_HEIGHT_PX, bg=c.COLOR_MIDNIGHT_BLUE, highlightthickness=0)
        self.canvas.pack()
        self.canvas.create_text(275, 25, text="Your field:", font=tkutils.get_font("main"), fill=c.COLOR_CLOUDS)
        self.canvas.create_text(925, 25, text="Enemy's field:", font=tkutils.get_font("main"), fill=c.COLOR_CLOUDS)

        my_field_canvas_container = tk.Canvas(self.canvas, width=11 * c.TILE_SIZE_PX, height=11 * c.TILE_SIZE_PX, bg=c.COLOR_SILVER, highlightthickness=0)
        my_field_canvas_container.place(x=0, y=c.TILE_SIZE_PX)

        self.my_field_canvas = tk.Canvas(my_field_canvas_container, width=10 * c.TILE_SIZE_PX, height=10 * c.TILE_SIZE_PX, bg=c.COLOR_SILVER, highlightthickness=0)
        self.my_field_canvas.place(x=c.TILE_SIZE_PX, y=c.TILE_SIZE_PX)

        enemy_field_canvas_container = tk.Canvas(self.canvas, width=11 * c.TILE_SIZE_PX, height=11 * c.TILE_SIZE_PX, bg=c.COLOR_SILVER, highlightthickness=0)
        enemy_field_canvas_container.place(x=13*c.TILE_SIZE_PX, y=1*c.TILE_SIZE_PX)

        self.enemy_field_canvas = tk.Canvas(enemy_field_canvas_container, width=10 * c.TILE_SIZE_PX, height=10 * c.TILE_SIZE_PX, bg=c.COLOR_SILVER, highlightthickness=0)
        self.enemy_field_canvas.place(x=c.TILE_SIZE_PX, y=c.TILE_SIZE_PX)

        for field_container in [my_field_canvas_container, enemy_field_canvas_container]:
            for x in range(10):
                field_container.create_line(0, (1 + x) * c.TILE_SIZE_PX, 11 * c.TILE_SIZE_PX, (1 + x) * c.TILE_SIZE_PX, fill=c.COLOR_MIDNIGHT_BLUE)
                field_container.create_line((x + 1) * c.TILE_SIZE_PX, 0, (x + 1) * c.TILE_SIZE_PX, 12 * c.TILE_SIZE_PX, fill=c.COLOR_MIDNIGHT_BLUE)
                field_container.create_text((x + 1.5) * c.TILE_SIZE_PX, 0.5 * c.TILE_SIZE_PX, text=chr(65 + x), font=tkutils.get_font("main"), fill=c.COLOR_MIDNIGHT_BLUE)
                field_container.create_text(0.5 * c.TILE_SIZE_PX, (x + 1.5) * c.TILE_SIZE_PX, text=1 + x, font=tkutils.get_font("main"), fill=c.COLOR_MIDNIGHT_BLUE)

        # init tiles
        for x in range(10):
            for y in range(10):
                draw_tile(self.my_field_canvas, x, y, "", font=tkutils.get_font("main"))
                draw_tile(self.enemy_field_canvas, x, y, "", font=tkutils.get_font("main"))

        self.my_field_canvas.bind('<Motion>', lambda event: controller.my_field_canvas_mouse_motion(event))
        self.my_field_canvas.bind('<Button-1>', lambda event: controller.my_field_canvas_click(event))
        self.enemy_field_canvas.bind('<Motion>', lambda event: controller.enemy_field_canvas_mouse_motion(event))
        self.enemy_field_canvas.bind('<Button-1>', lambda event: controller.enemy_field_canvas_click(event))
        self.canvas.bind_all('<Key>', lambda event: controller.key_press(event))

    def update_my_field(self, game):
        font = tkutils.get_font("main")
        for x in range(10):
            for y in range(10):
                draw_tile(self.my_field_canvas, x, y, game.my_field.get_state(x, y), font=font)

    def update_enemy_field(self, game):
        font = tkutils.get_font("main")
        for x in range(10):
            for y in range(10):
                draw_tile(self.enemy_field_canvas, x, y, game.enemy_field.get_state(x, y), font=font)

    def update_caption(self, game):
        self.canvas.create_rectangle(500, 0, 700, 50, fill=c.COLOR_MIDNIGHT_BLUE, outline="")
        text = {
            0: "Waiting for connection",
            1: "Place your ships",
            2: "Waiting for enemy",
            3: "Your turn",
            4: "Enemy's turn",
            5: "You won!",
            6: "You lost :(",
        }[game.phase]
        self.canvas.create_text(600, 25, text=text, font=tkutils.get_font("secondary"), fill=c.COLOR_CLOUDS)

    def update_view(self, game):
        self.update_my_field(game)
        self.update_enemy_field(game)
        self.update_caption(game)

    def clear_ghost_ship(self, x, y, length, orientation):
        for i in range(length):
            if orientation == Orientation.HORIZONTAL:
                draw_tile(self.my_field_canvas, x + i, y, "", font=tkutils.get_font("main"))
            else:
                draw_tile(self.my_field_canvas, x, y + i, "", font=tkutils.get_font("main"))

    def show_ghost_ship(self, x, y, length, orientation):
        for i in range(length):
            if orientation == Orientation.HORIZONTAL:
                draw_tile(self.my_field_canvas, x + i, y, "g", font=tkutils.get_font("main"))
            else:
                draw_tile(self.my_field_canvas, x, y + i, "g", font=tkutils.get_font("main"))


def draw_tile(canvas, x, y, tile_state, font):
    color = c.COLOR_CLOUDS
    if tile_state == "X":
        color = c.COLOR_ALIZARIN
    if tile_state == " ":
        color = c.COLOR_PETER_RIVER
    if tile_state == ".":
        color = c.COLOR_CONCRETE
        tile_state = "∙"
    if tile_state == "g":
        color = c.COLOR_PETER_RIVER_05
        tile_state = ""
    canvas.create_rectangle(c.TILE_SIZE_PX * x, c.TILE_SIZE_PX * y,
                            c.TILE_SIZE_PX * (x + 1), c.TILE_SIZE_PX * (y + 1),
                            fill=color, outline=c.COLOR_MIDNIGHT_BLUE)
    canvas.create_text((x + 0.5) * c.TILE_SIZE_PX, (y + 0.5) * c.TILE_SIZE_PX, text=tile_state,
                       font=font, fill=c.COLOR_MIDNIGHT_BLUE)

