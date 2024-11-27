# File: Classes/ASCIIArtGenerator.py

import pyfiglet
from colorama import Fore, Style


# File: Classes/ASCIIArtGenerator.py

import pyfiglet
from colorama import Fore, Style


class ASCIIArtGenerator:
    def __init__(self):
        self.font = None
        self.color = Fore.WHITE
        self.width = 80
        self.height = 10  # Added a default height
        self.custom_char = '#'

    def set_font(self, font):
        self.font = font

    def set_color(self, color):
        self.color = color

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height  # Added a setter for height

    def set_custom_char(self, custom_char):
        self.custom_char = custom_char

    def generate_art(self, text):
        ascii_art = pyfiglet.figlet_format(text, font=self.font, width=self.width)
        # Limiting the height of the ASCII art
        ascii_art_lines = ascii_art.split('\n')[:self.height]
        return '\n'.join(ascii_art_lines).replace('#', self.custom_char)

    def apply_color(self, ascii_art):
        return self.color + ascii_art + Style.RESET_ALL

    def get_dimensions(self):
        # Get user input for width and height
        while True:
            try:
                width = int(input("Enter the width of the ASCII art (between 10 and 200): "))
                if 10 <= width <= 200:
                    self.set_width(width)
                    break
                else:
                    print("Width must be between 10 and 200.")
            except ValueError:
                print("Please enter a valid integer.")

        while True:
            try:
                height = int(input("Enter the height of the ASCII art (between 1 and 50): "))
                if 1 <= height <= 50:
                    self.set_height(height)
                    break
                else:
                    print("Height must be between 1 and 50.")
            except ValueError:
                print("Please enter a valid integer.")


