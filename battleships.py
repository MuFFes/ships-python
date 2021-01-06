import constants
import assets
import Controllers.maincontroller


def draw_tile(canvas, x, y, tile_type, font):
    color = constants.COLOR_CLOUDS
    if tile_type == "X":
        color = constants.COLOR_ALIZARIN
    if tile_type == " ":
        color = constants.COLOR_PETER_RIVER
    if tile_type == ".":
        color = constants.COLOR_CONCRETE
    canvas.create_rectangle(constants.TILE_SIZE_PX * x, constants.TILE_SIZE_PX * y,
                            constants.TILE_SIZE_PX * (x + 1), constants.TILE_SIZE_PX * (y + 1),
                            fill=color, outline=constants.COLOR_MIDNIGHT_BLUE)
    canvas.create_text((x + 1.5) * constants.TILE_SIZE_PX, (y + 2.5) * constants.TILE_SIZE_PX, text=tile_type,
                       font=font, fill=constants.COLOR_MIDNIGHT_BLUE)


def infield(x, y):
    if 2 * constants.TILE_SIZE_PX < y < 12 * constants.TILE_SIZE_PX:
        if constants.TILE_SIZE_PX < x < 11 * constants.TILE_SIZE_PX:
            return True
        if constants.TILE_SIZE_PX * (12 + constants.FIELD_SPACING) < x < constants.TILE_SIZE_PX * (
                22 + constants.FIELD_SPACING):
            return True
    return False


if __name__ == '__main__':
    assets.Assets.load()
    controller = Controllers.maincontroller.MainController()
