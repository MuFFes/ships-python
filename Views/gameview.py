import tkinter as tk

import constants
import tkutils
from battleships import infield, draw_tile


class GameView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas = tk.Canvas(self, width=constants.WINDOW_WIDTH_PX, height=constants.WINDOW_HEIGHT_PX, bg=constants.COLOR_MIDNIGHT_BLUE, highlightthickness=0)
        canvas.pack()
        canvas.create_text(275, 25, text="Your field:", font=tkutils.get_font("main"), fill=constants.COLOR_CLOUDS)
        canvas.create_text(600, 25, text="Enemy's turn", font=tkutils.get_font("secondary"), fill=constants.COLOR_CLOUDS)
        canvas.create_text(925, 25, text="Enemy's field:", font=tkutils.get_font("main"), fill=constants.COLOR_CLOUDS)

        my_field_canvas_container = tk.Canvas(canvas, width=11 * constants.TILE_SIZE_PX, height=11 * constants.TILE_SIZE_PX, bg=constants.COLOR_SILVER, highlightthickness=0)
        my_field_canvas_container.place(x=0, y=constants.TILE_SIZE_PX)

        my_field_canvas = tk.Canvas(my_field_canvas_container, width=10 * constants.TILE_SIZE_PX, height=10 * constants.TILE_SIZE_PX, bg=constants.COLOR_SILVER, highlightthickness=0)
        my_field_canvas.place(x=constants.TILE_SIZE_PX, y=constants.TILE_SIZE_PX)

        enemy_field_canvas_container = tk.Canvas(canvas, width=11 * constants.TILE_SIZE_PX, height=11 * constants.TILE_SIZE_PX, bg=constants.COLOR_SILVER, highlightthickness=0)
        enemy_field_canvas_container.place(x=13*constants.TILE_SIZE_PX, y=1*constants.TILE_SIZE_PX)

        enemy_field_canvas = tk.Canvas(enemy_field_canvas_container, width=10 * constants.TILE_SIZE_PX, height=10 * constants.TILE_SIZE_PX, bg=constants.COLOR_SILVER, highlightthickness=0)
        enemy_field_canvas.place(x=constants.TILE_SIZE_PX, y=constants.TILE_SIZE_PX)

        # init tiles
        for x in range(10):
            for y in range(10):
                draw_tile(my_field_canvas, x, y, "", font=constants.FONT_MAIN)
                draw_tile(enemy_field_canvas, x, y, "", font=constants.FONT_MAIN)

        for field_container in [my_field_canvas_container, enemy_field_canvas_container]:
            for x in range(10):
                field_container.create_line(0, (1 + x) * constants.TILE_SIZE_PX, 11 * constants.TILE_SIZE_PX, (1 + x) * constants.TILE_SIZE_PX, fill=constants.COLOR_MIDNIGHT_BLUE)
                field_container.create_line((x + 1) * constants.TILE_SIZE_PX, 0, (x + 1) * constants.TILE_SIZE_PX, 12 * constants.TILE_SIZE_PX, fill=constants.COLOR_MIDNIGHT_BLUE)
                field_container.create_text((x + 1.5) * constants.TILE_SIZE_PX, 0.5 * constants.TILE_SIZE_PX, text=chr(65 + x), font=tkutils.get_font("main"), fill=constants.COLOR_MIDNIGHT_BLUE)
                field_container.create_text(0.5 * constants.TILE_SIZE_PX, (x + 1.5) * constants.TILE_SIZE_PX, text=1 + x, font=tkutils.get_font("main"), fill=constants.COLOR_MIDNIGHT_BLUE)

    #     controller.bind('<Motion>', self.motion)
    #
    # def motion(self, event):
    #     if infield(event.x, event.y):
    #         self.controller.config(cursor="hand2")
    #     else:
    #         self.controller.config(cursor="arrow")
