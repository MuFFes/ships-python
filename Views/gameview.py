import tkinter as tk

import constants
from battleships import infield, draw_tile


class GameView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas = tk.Canvas(self, width=constants.WINDOW_WIDTH_PX, height=constants.WINDOW_HEIGHT_PX, bg=constants.COLOR_MIDNIGHT_BLUE)
        canvas.pack()
        canvas.create_text(275, 25, text="Your field:", font=controller.get_font("main"), fill=constants.COLOR_CLOUDS)
        canvas.create_text(600, 25, text="Enemy's turn", font=controller.get_font("secondary"), fill=constants.COLOR_CLOUDS)
        canvas.create_text(925, 25, text="Enemy's field:", font=controller.get_font("main"), fill=constants.COLOR_CLOUDS)
        canvas.create_rectangle(0, 50, 550, 600, fill=constants.COLOR_SILVER, outline="")
        canvas.create_rectangle(650, 50, 1200, 600, fill=constants.COLOR_SILVER, outline="")

        # init tiles
        for field in range(2):
            for x in range(10):
                for y in range(10):
                    draw_tile(canvas, x, y, field, "", font=constants.FONT_MAIN)

        for x in range(10):
            canvas.create_line(0, (2 + x) * constants.TILE_SIZE_PX, 11 * constants.TILE_SIZE_PX, (2 + x) * constants.TILE_SIZE_PX,
                               fill=constants.COLOR_MIDNIGHT_BLUE)
            canvas.create_line((1 + x) * constants.TILE_SIZE_PX, 1 * constants.TILE_SIZE_PX, (1 + x) * constants.TILE_SIZE_PX,
                               12 * constants.TILE_SIZE_PX, fill=constants.COLOR_MIDNIGHT_BLUE)
            canvas.create_text((x + 1.5) * constants.TILE_SIZE_PX, 1.5 * constants.TILE_SIZE_PX, text=chr(65 + x),
                               font=controller.get_font("main"), fill=constants.COLOR_MIDNIGHT_BLUE)
            canvas.create_text(0.5 * constants.TILE_SIZE_PX, (x + 2.5) * constants.TILE_SIZE_PX, text=1 + x,
                               font=controller.get_font("main"),
                               fill=constants.COLOR_MIDNIGHT_BLUE)

        for x in range(10):
            canvas.create_line((11 + constants.FIELD_SPACING) * constants.TILE_SIZE_PX, (2 + x) * constants.TILE_SIZE_PX,
                               (22 + constants.FIELD_SPACING) * constants.TILE_SIZE_PX, (2 + x) * constants.TILE_SIZE_PX,
                               fill=constants.COLOR_MIDNIGHT_BLUE)
            canvas.create_line((12 + constants.FIELD_SPACING + x) * constants.TILE_SIZE_PX, 1 * constants.TILE_SIZE_PX,
                               (12 + constants.FIELD_SPACING + x) * constants.TILE_SIZE_PX, 12 * constants.TILE_SIZE_PX,
                               fill=constants.COLOR_MIDNIGHT_BLUE)
            canvas.create_text((x + constants.FIELD_SPACING + 12.5) * constants.TILE_SIZE_PX, 1.5 * constants.TILE_SIZE_PX,
                               text=chr(65 + x), font=controller.get_font("main"), fill=constants.COLOR_MIDNIGHT_BLUE)
            canvas.create_text((constants.FIELD_SPACING + 11.5) * constants.TILE_SIZE_PX, (x + 2.5) * constants.TILE_SIZE_PX,
                               text=1 + x, font=controller.get_font("main"), fill=constants.COLOR_MIDNIGHT_BLUE)

        controller.bind('<Motion>', self.motion)

    def motion(self, event):
        if infield(event.x, event.y):
            self.controller.config(cursor="pirate")
        else:
            self.controller.config(cursor="arrow")
