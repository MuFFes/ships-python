import tkinter as tk

import constants as c
import tkutils


class GameView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width=c.WINDOW_WIDTH_PX, height=c.WINDOW_HEIGHT_PX, bg=c.COLOR_MIDNIGHT_BLUE, highlightthickness=0)
        canvas.pack()
        canvas.create_text(275, 25, text="Your field:", font=tkutils.get_font("main"), fill=c.COLOR_CLOUDS)
        canvas.create_text(600, 25, text="Place your ships", font=tkutils.get_font("secondary"), fill=c.COLOR_CLOUDS)
        canvas.create_text(925, 25, text="Enemy's field:", font=tkutils.get_font("main"), fill=c.COLOR_CLOUDS)

        my_field_canvas_container = tk.Canvas(canvas, width=11 * c.TILE_SIZE_PX, height=11 * c.TILE_SIZE_PX, bg=c.COLOR_SILVER, highlightthickness=0)
        my_field_canvas_container.place(x=0, y=c.TILE_SIZE_PX)

        self.my_field_canvas = tk.Canvas(my_field_canvas_container, width=10 * c.TILE_SIZE_PX, height=10 * c.TILE_SIZE_PX, bg=c.COLOR_SILVER, highlightthickness=0)
        self.my_field_canvas.place(x=c.TILE_SIZE_PX, y=c.TILE_SIZE_PX)

        enemy_field_canvas_container = tk.Canvas(canvas, width=11 * c.TILE_SIZE_PX, height=11 * c.TILE_SIZE_PX, bg=c.COLOR_SILVER, highlightthickness=0)
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

        canvas.bind('<Button-1>', lambda event: controller.shoot(event))

        self.my_field_canvas.bind('<Enter>', lambda event: change_cursor(controller, cursor="hand2"))
        self.my_field_canvas.bind('<Leave>', lambda event: change_cursor(controller, cursor="arrow"))
        self.enemy_field_canvas.bind('<Enter>', lambda event: change_cursor(controller, cursor="hand2"))
        self.enemy_field_canvas.bind('<Leave>', lambda event: change_cursor(controller, cursor="arrow"))

    def update_view(self, game):
        for x in range(10):
            for y in range(10):
                draw_tile(self.my_field_canvas, x, y, game.my_field.get_state(x, y), font=tkutils.get_font("main"))
                draw_tile(self.enemy_field_canvas, x, y, game.enemy_field.get_state(x, y), font=tkutils.get_font("main"))

    def update_fields(self):
        pass


def change_cursor(controller, cursor):
    controller.root.config(cursor=cursor)


def draw_tile(canvas, x, y, tile_state, font):
    color = c.COLOR_CLOUDS
    if tile_state == "X":
        color = c.COLOR_ALIZARIN
    if tile_state == " ":
        color = c.COLOR_PETER_RIVER
    if tile_state == ".":
        color = c.COLOR_CONCRETE
    canvas.create_rectangle(c.TILE_SIZE_PX * x, c.TILE_SIZE_PX * y,
                            c.TILE_SIZE_PX * (x + 1), c.TILE_SIZE_PX * (y + 1),
                            fill=color, outline=c.COLOR_MIDNIGHT_BLUE)
    if tile_state == ".":
        tile_state = "∙"
    canvas.create_text((x + 0.5) * c.TILE_SIZE_PX, (y + 0.5) * c.TILE_SIZE_PX, text=tile_state,
                       font=font, fill=c.COLOR_MIDNIGHT_BLUE)

