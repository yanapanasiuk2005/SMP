from Data.Lab3.Classes.ASCIIArtGenerator import ASCIIArtGenerator
from Data.Lab3.Constants.colors import COLORS
from Data.Lab3.Functions.utils import get_terminal_width, save_to_file, center_text
from Shared.Settings import initialize_app
from Data.Lab3.Interfaces.menu import display_main_menu


def main3():
    initialize_app()

    user_input, font_choice, color_choice = display_main_menu()

    ascii_gen = ASCIIArtGenerator()
    ascii_gen.set_font(font_choice)
    ascii_gen.set_color(COLORS[color_choice])
    ascii_gen.set_width(get_terminal_width())
    ascii_gen.set_custom_char(input("Enter the custom character: "))

    # Generate ASCII Art
    ascii_art = ascii_gen.generate_art(user_input)
    colored_art = ascii_gen.apply_color(ascii_art)

    # Center and display
    print(center_text(colored_art, get_terminal_width()))

    # Ask to save
    if input("Do you want to save this art? (yes/no): ").lower() == "yes":
        filename = input("Enter filename to save: ")
        save_to_file(filename, colored_art)