def get_user_input():
    user_input = input("Enter a word or phrase to convert to ASCII art: ")

    while True:
        color_option = input("Choose color option (black_and_white, grayscale): ").lower()
        if color_option in ["black_and_white", "grayscale"]:
            break
        else:
            print("Invalid option. Please enter 'black_and_white' or 'grayscale'.")

    color_symbols = define_custom_symbols(color_option)

    while True:
        try:
            width = int(input("Enter the desired width of the ASCII art (between 20 and 200): "))
            if 20 <= width <= 200:
                break
            else:
                print("Please enter a width between 20 and 200.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    while True:
        try:
            height = int(input("Enter the desired height of the ASCII art (between 5 and 50): "))
            if 5 <= height <= 50:
                break
            else:
                print("Please enter a height between 5 and 50.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    while True:
        alignment = input("Enter text alignment (left, center, right): ").lower()
        if alignment in ["left", "center", "right"]:
            break
        else:
            print("Invalid alignment. Please enter 'left', 'center', or 'right'.")

    return user_input, color_symbols, width, height, alignment, color_option


def define_custom_symbols(color_option):
    symbols = {}

    if color_option == "black_and_white":

        black_symbol = input("Enter a symbol for black areas: ")
        white_symbol = input("Enter a symbol for white areas: ")
        symbols['black'] = [black_symbol]
        symbols['white'] = [white_symbol, ' ']

    elif color_option == "grayscale":
        symbols['grayscale'] = []
        for i in range(5):
            shade_symbol = input(f"Enter a symbol for shade {i + 1} (from dark to light): ")
            symbols['grayscale'].append(shade_symbol)

    return symbols
