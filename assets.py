import pyglet


class Assets:
    @staticmethod
    def load():
        Assets.load_font("fonts/PermanentMarker.ttf")
        Assets.load_font("fonts/InconsolataExpanded-Regular.ttf")
        Assets.load_font("fonts/FiraCode-Regular.ttf")

    @staticmethod
    def load_font(fontpath):
        try:
            pyglet.font.add_file(fontpath)
        except:
            print(f"Error loading font from {fontpath}")
