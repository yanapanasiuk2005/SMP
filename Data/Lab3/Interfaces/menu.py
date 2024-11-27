# File: Interfaces/menu.py
from Data.Lab3.Constants.colors import COLORS
from Data.Lab3.Constants.fonts import FONTS
from Data.Lab3.Functions.utils import get_user_input


def display_main_menu():
    """Display the main menu and guide the user through the steps."""
    print("Step 1: Enter a word or phrase to convert to ASCII art:")
    user_input = input()

    print("\nStep 2: Choose a font from the list below:")
    for index, font in enumerate(FONTS, start=1):
        print(f" {index}. {font}")

    font_choice_index = get_user_input(f"Enter the number corresponding to your font choice (1-{len(FONTS)}): ",
                                       [str(i) for i in range(1, len(FONTS) + 1)])
    font_choice = FONTS[int(font_choice_index) - 1]

    print("\nStep 3: Choose a color:")
    for color in COLORS.keys():
        print(f" - {color}")

    color_choice = get_user_input("Enter your color choice: ", COLORS.keys())

    return user_input, font_choice, color_choice

def get_validated_dimension_input(dimension_name, min_value, max_value):
    """Helper function to get a validated dimension input."""
    while True:
        try:
            dimension = int(input(f"Enter the {dimension_name} (between {min_value} and {max_value}): "))
            if min_value <= dimension <= max_value:
                return dimension
            else:
                print(f"The {dimension_name} must be between {min_value} and {max_value}.")
        except ValueError:
            print(f"Please enter a valid integer for {dimension_name}.")
