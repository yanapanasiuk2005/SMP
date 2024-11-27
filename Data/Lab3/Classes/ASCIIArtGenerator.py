# File: Classes/ASCIIArtGenerator.py

import pyfiglet
from colorama import Fore, Style


class ASCIIArtGenerator:
    def __init__(self):
        self.font = None
        self.color = Fore.WHITE
        self.width = 80
        self.custom_char = '#'

    def set_font(self, font):
        self.font = font

    def set_color(self, color):
        self.color = color

    def set_width(self, width):
        self.width = width

    def set_custom_char(self, custom_char):
        self.custom_char = custom_char

    def generate_art(self, text):
        ascii_art = pyfiglet.figlet_format(text, font=self.font, width=self.width)
        return ascii_art.replace('#', self.custom_char)

    def apply_color(self, ascii_art):
        return self.color + ascii_art + Style.RESET_ALL

