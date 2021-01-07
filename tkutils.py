import tkinter as tk
import tkinter.font
import constants

# TODO: STORE FONTS


def character_limit(entry_text, limit):
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[:limit])


def get_font(font_type):
    return {
        "main": tk.font.Font(**constants.FONT_MAIN),
        "title": tk.font.Font(**constants.FONT_TITLE),
        "secondary": tk.font.Font(**constants.FONT_SECONDARY),
        "monospace": tk.font.Font(**constants.FONT_MONOSPACE)
    }[font_type]
